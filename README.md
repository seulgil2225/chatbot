# 💻 mySUNI 총무 챗봇

mySUNI 조직의 총무 업무 자동화를 위한 AI 챗봇입니다.

## 🎯 주요 기능

- 🚗 **주차등록 안내**: 주차 신청 절차 자동 안내
- 🎫 **임시출입증 발급**: 출입증 발급 방법 상세 안내
- 👥 **담당자 안내**: 시설관리, 강의장, 회의실 담당자 정보 제공
- 🏢 **총무 업무 문의**: 15개 FAQ 기반 자동 응답
- 🤖 **AI 답변**: Gemini API 활용한 자연스러운 대화

## 📊 FAQ 데이터

현재 **15개의 총무 업무 FAQ**가 준비되어 있습니다:
- 주차 및 차량 관련 (2개)
- 출입 및 방문자 관리 (3개)
- 시설 및 공간 관리 (4개)
- 일반 안내 (6개)

## 🛠️ 기술 스택

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash
- **Data**: 텍스트 파일 기반 FAQ
- **Language**: Python 3.13

## 📦 설치 방법

### 1. 저장소 클론
```bash
git clone [your-repo-url]
cd chatbot
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정
`.env` 파일을 생성하고 Gemini API 키를 입력하세요:
```env
GEMINI_API_KEY=your_api_key_here
```

API 키 발급: https://makersuite.google.com/app/apikey

### 4. 실행
```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501` 접속

## 🌐 온라인 배포 (QR코드용)

### 📱 QR코드 사이트로 배포하기

**1단계: Streamlit Cloud 배포**
```bash
# GitHub 저장소 생성 후
git init
git add .
git commit -m "Deploy mySUNI chatbot"
git push -u origin main
```

**2단계: Streamlit Cloud 설정**
- https://share.streamlit.io 접속
- GitHub 연동 후 앱 배포
- Settings > Secrets에서 API 키 설정:
```toml
GEMINI_API_KEY = "your_api_key_here"
```

**3단계: QR코드 생성**
```bash
# generate_qr.py에서 URL 설정 후
python generate_qr.py
```

**4단계: QR코드 배포**
- 생성된 `mysuni_chatbot_qr.png`를 인쇄
- 포스터/명함/스티커로 제작
- 사무실 곳곳에 부착

📖 **상세 가이드**: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) 참고

## 📝 FAQ 업데이트 방법

`mySUNI_FAQ.txt` 파일을 수정하여 FAQ를 추가/수정할 수 있습니다:

```
[질문N]
Q: 질문 내용?
A: 답변 내용
```

## 🎨 커스터마이징

### 아이콘 변경
- 브라우저 탭: `app.py`의 `page_icon` 수정
- 챗봇 아이콘: `sunny_character.png` 교체
- 사용자 아이콘: `avatar` 파라미터 수정

### FAQ 카테고리 추가
`mySUNI_FAQ.txt`에 새로운 카테고리 섹션 추가

## 📞 문의

총무 업무 관련 추가 문의: 이슬기PM

---

**개발 기간**: 2025년 1월
**버전**: 1.0.0
**담당자**: 이슬기PM

