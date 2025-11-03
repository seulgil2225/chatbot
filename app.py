"""
mySUNI 총무 업무 자동 응답 챗봇
- 임시출입증, 주차등록 등 반복 문의 자동화
- FAQ 기반 자동 응답
- Gemini API를 활용한 자연어 응답
"""

import streamlit as st
import os
from dotenv import load_dotenv
from datetime import datetime
import google.generativeai as genai

# 환경 변수 로드
load_dotenv()

# Gemini API 설정 (Streamlit Cloud Secrets 우선)
GEMINI_API_KEY = None
try:
    # Streamlit Cloud Secrets에서 읽기 (배포 환경)
    GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")
except:
    # .env 파일에서 읽기 (로컬 환경)
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# FAQ 데이터 로드 함수
@st.cache_data(ttl=60)  # 60초마다 캐시 갱신 (파일 수정 반영)
def load_faq_data():
    """mySUNI_FAQ.txt 파일에서 FAQ 데이터를 읽어옵니다."""
    try:
        with open("mySUNI_FAQ.txt", "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "FAQ 파일을 찾을 수 없습니다."

# Gemini로 답변 생성 함수
def generate_response(user_question, faq_data):
    """FAQ 데이터를 기반으로 사용자 질문에 답변을 생성합니다."""
    
    if not GEMINI_API_KEY:
        return "⚠️ Gemini API 키가 설정되지 않았습니다. .env 파일을 확인해주세요."
    
    try:
        # Gemini 모델 초기화 (2025년 최신 버전)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # 프롬프트 구성
        prompt = f"""당신은 mySUNI의 친절한 총무 담당자입니다. 아래 FAQ 데이터를 참고하여 사용자의 질문에 정확하고 친절하게 답변해주세요.

**중요 규칙:**
1. FAQ에 있는 정보를 최우선으로 참고하세요
2. 친절하고 공손한 말투로 답변하세요 (존댓말 사용)
3. 답변은 명확하고 구체적으로 작성하세요
4. FAQ에 없는 내용이면 "해당 내용은 FAQ에 없습니다. 이슬기PM에게 직접 문의해주세요."라고 안내하세요
5. 단계별 절차가 있다면 번호를 매겨서 설명하세요

**FAQ 데이터:**
{faq_data}

**사용자 질문:**
{user_question}

**답변:**"""
        
        # Gemini API 호출
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"⚠️ 답변 생성 중 오류가 발생했습니다: {str(e)}\n\n이슬기PM에게 직접 문의해주세요."

# 페이지 설정
st.set_page_config(
    page_title="mySUNI 총무 챗봇",
    page_icon="💻",
    layout="wide",  # 모바일에서 더 넓은 화면 활용
    initial_sidebar_state="collapsed"  # QR코드 접속 시 사이드바 숨김
)

# 모바일 최적화 CSS
st.markdown("""
<style>
    /* 모바일 최적화 */
    .stChatFloatingInputContainer {
        bottom: 20px;
    }
    
    /* 입력창 크기 조정 */
    .stChatInputContainer {
        padding: 1rem;
    }
    
    /* 모바일에서 여백 조정 */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    }
    
    /* 메시지 말풍선 최적화 */
    .stChatMessage {
        padding: 0.5rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

# 제목 및 설명
st.title("💻 mySUNI 총무 챗봇")
st.markdown("**임시출입증, 주차등록 등 총무 관련 문의사항을 편하게 질문하세요!**")
st.divider()

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []
    # 환영 메시지
    st.session_state.messages.append({
        "role": "assistant",
        "content": "안녕하세요! mySUNI 총무 챗봇입니다. 😊\n\n임시출입증 발급, 주차등록, 사무실 안내 등 총무 업무 관련 질문을 해주세요!"
    })

# 대화 히스토리 표시
for message in st.session_state.messages:
    # 아이콘 설정: 챗봇은 써니 캐릭터, 사용자는 밝은 피부톤 손든 사람 이모지
    avatar = "sunny_character.png" if message["role"] == "assistant" else "🙋🏻"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# FAQ 데이터 로드
faq_data = load_faq_data()

# 사용자 입력
if prompt := st.chat_input("총무 관련 질문을 입력하세요..."):
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🙋🏻"):
        st.markdown(prompt)
    
    # Gemini API로 답변 생성 (써니 캐릭터 아이콘)
    with st.chat_message("assistant", avatar="sunny_character.png"):
        with st.spinner("답변을 생성하는 중..."):
            response = generate_response(prompt, faq_data)
            st.markdown(response)
    
    # 어시스턴트 메시지 추가
    st.session_state.messages.append({"role": "assistant", "content": response})

# 사이드바 정보
with st.sidebar:
    st.header("📌 챗봇 정보")
    st.markdown("""
    **주요 기능:**
    - 🎫 임시출입증 발급 안내
    - 🚗 주차등록 절차 안내
    - 🏢 사무실 위치 및 시설 안내
    - 📝 기타 총무 업무 문의
    
    **개발 상태:**
    - ✅ 기본 UI 완성
    - ✅ Gemini API 연결 완료
    - ✅ FAQ 데이터 (15개) 준비 완료
    - ✅ 자동 답변 시스템 작동 중
    """)
    
    if st.button("대화 내역 지우기"):
        st.session_state.messages = []
        st.rerun()

# 하단 안내
st.divider()
st.caption("💡 챗봇이 답변하지 못하는 경우, 총무 담당자에게 직접 문의해주세요.")

