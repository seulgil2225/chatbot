# 📁 mySUNI 챗봇 프로젝트 구조

QR코드 배포용으로 최적화된 프로젝트 파일 구조입니다.

---

## 📂 파일 및 디렉토리 구조

```
chatbot/
├── 📄 app.py                          # 메인 챗봇 애플리케이션 (Streamlit)
├── 📄 mySUNI_FAQ.txt                  # FAQ 데이터베이스 (15개 질문/답변)
│
├── 🚀 배포 관련 파일
│   ├── requirements.txt               # Python 패키지 의존성
│   ├── .gitignore                     # Git 제외 파일 설정
│   ├── .env                           # 로컬 환경 변수 (API 키, Git 제외됨)
│   └── .streamlit/
│       ├── config.toml                # Streamlit 설정 (테마, 서버)
│       └── secrets.toml.example       # Secrets 템플릿
│
├── 📱 QR코드 관련 파일
│   ├── generate_qr.py                 # QR코드 자동 생성 스크립트
│   ├── mysuni_chatbot_qr.png          # 생성된 QR코드 이미지
│   └── qr_poster_template.html        # 인쇄용 포스터 템플릿
│
├── 🎨 디자인 에셋
│   ├── sunny_character.png            # 써니 캐릭터 (챗봇 아이콘)
│   └── 써니안내캐릭터.PNG              # 원본 캐릭터 이미지
│
└── 📖 문서
    ├── README.md                      # 프로젝트 개요 및 기본 설치
    ├── QUICKSTART.md                  # 빠른 시작 가이드 (10분 배포)
    ├── DEPLOYMENT_GUIDE.md            # 상세 배포 가이드
    ├── PROJECT_STRUCTURE.md           # 이 파일 (프로젝트 구조 설명)
    └── 이슬기_package_v1.md            # 초기 기획 문서
```

---

## 📄 주요 파일 설명

### 1. **app.py** (핵심 애플리케이션)
- **역할**: Streamlit 기반 챗봇 웹 애플리케이션
- **주요 기능**:
  - Gemini API 연동 (자연어 처리)
  - FAQ 데이터 로드 및 검색
  - 대화 히스토리 관리
  - 모바일 최적화 UI
- **배포 대상**: Streamlit Cloud에서 실행

### 2. **mySUNI_FAQ.txt** (지식 베이스)
- **역할**: 챗봇이 참조하는 FAQ 데이터베이스
- **형식**:
```
[질문1]
Q: 주차등록은 어떻게 하나요?
A: 주차등록 절차...
```
- **수정 방법**: 텍스트 편집기로 직접 수정 가능
- **반영 시간**: 60초 (캐시 TTL)

### 3. **generate_qr.py** (QR코드 생성기)
- **역할**: 배포된 챗봇 URL을 QR코드로 변환
- **사용법**:
  1. `CHATBOT_URL` 변수에 실제 URL 입력
  2. `python generate_qr.py` 실행
  3. `mysuni_chatbot_qr.png` 생성됨
- **옵션**: 써니 캐릭터 로고 자동 삽입

### 4. **requirements.txt** (패키지 관리)
- **역할**: Python 패키지 의존성 명시
- **주요 패키지**:
  - `streamlit>=1.35.0` (웹 프레임워크)
  - `google-generativeai>=0.8.0` (Gemini API)
  - `qrcode[pil]>=7.4.2` (QR코드 생성)
  - `python-dotenv>=1.0.0` (환경 변수)
- **자동 설치**: Streamlit Cloud 배포 시 자동 실행

### 5. **.gitignore** (보안)
- **역할**: 민감한 파일을 Git 커밋에서 제외
- **제외 대상**:
  - `.env` (API 키)
  - `.streamlit/secrets.toml` (배포 환경 변수)
  - `__pycache__/` (Python 캐시)
  - `.vscode/`, `.idea/` (IDE 설정)

---

## 🚀 배포 흐름도

```
로컬 개발                  GitHub                  Streamlit Cloud
┌─────────────┐          ┌─────────────┐          ┌─────────────┐
│             │          │             │          │             │
│  app.py     │  git     │  Repository │  auto    │  Live App   │
│  FAQ.txt    │  push    │  (public)   │  deploy  │  (URL)      │
│  .env       │  ────▶   │             │  ────▶   │             │
│             │          │             │          │             │
└─────────────┘          └─────────────┘          └─────────────┘
      │                        │                        │
      │                        │                        ▼
      ▼                        │                  ┌─────────────┐
┌─────────────┐                │                  │  Secrets    │
│ generate_qr │                │                  │  (API Key)  │
│     .py     │                │                  └─────────────┘
└─────────────┘                │
      │                        │
      ▼                        │
┌─────────────┐                │
│  QR Code    │◀───────────────┘
│   (PNG)     │   scan URL
└─────────────┘
```

---

## 🔄 개발 워크플로우

### 로컬 개발 환경
```bash
# 1. 패키지 설치
pip install -r requirements.txt

# 2. 환경 변수 설정
echo "GEMINI_API_KEY=your_key" > .env

# 3. 로컬 실행
streamlit run app.py

# 4. 브라우저 접속
# http://localhost:8501
```

### 배포 환경 (Streamlit Cloud)
1. GitHub에 푸시
2. Streamlit Cloud 자동 배포
3. Secrets 설정 (웹 UI)
4. 앱 자동 재시작

---

## 📝 FAQ 업데이트 프로세스

### 방법 1: GitHub에서 직접 수정 (권장)
1. GitHub 저장소 접속
2. `mySUNI_FAQ.txt` 파일 편집
3. Commit changes
4. Streamlit Cloud 자동 재배포 (30초 소요)

### 방법 2: 로컬 수정 후 푸시
```bash
# 1. FAQ 파일 수정
nano mySUNI_FAQ.txt

# 2. Git 커밋
git add mySUNI_FAQ.txt
git commit -m "Update FAQ: 새로운 질문 추가"
git push

# 3. 자동 배포 대기
```

---

## 🎨 커스터마이징 포인트

### 1. 브랜드 색상 변경
**파일**: `.streamlit/config.toml`
```toml
[theme]
primaryColor = "#FF6B6B"        # 강조 색상
backgroundColor = "#FFFFFF"      # 배경색
```

### 2. 챗봇 아이콘 교체
**파일**: `app.py` (94줄)
```python
avatar = "sunny_character.png"  # 원하는 이미지로 교체
```

### 3. 환영 메시지 수정
**파일**: `app.py` (88줄)
```python
st.session_state.messages.append({
    "role": "assistant",
    "content": "환영 메시지를 여기에 작성하세요!"
})
```

---

## 🔐 보안 체크리스트

- [x] `.env` 파일이 `.gitignore`에 포함됨
- [x] API 키가 코드에 하드코딩되지 않음
- [x] Streamlit Secrets 사용 (배포 환경)
- [x] GitHub에 민감 정보 푸시 방지
- [x] HTTPS 자동 적용 (Streamlit Cloud)

---

## 📊 모니터링 및 분석

### Streamlit Cloud Analytics
- **접속 경로**: App > Analytics 탭
- **확인 가능 정보**:
  - 일별 방문자 수
  - 페이지 로딩 시간
  - 오류 발생 빈도
  - 리소스 사용량

### 로그 확인
- **실시간 로그**: App > Manage > Logs
- **디버깅**: 오류 메시지 및 스택 트레이스

---

## 🆘 문제 해결 참고 자료

| 문제 유형 | 참고 문서 |
|---------|---------|
| 배포 오류 | [QUICKSTART.md](QUICKSTART.md) - 자주 발생하는 오류 해결 섹션 |
| 상세 설정 | [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - 트러블슈팅 섹션 |
| 기능 추가 | [README.md](README.md) - 커스터마이징 섹션 |

---

## 📞 연락처

- **개발 담당**: 이슬기PM
- **프로젝트 버전**: 1.0.0
- **최종 업데이트**: 2025년 11월

---

**💡 팁**: 프로젝트를 복제하여 다른 부서의 챗봇으로 확장할 수 있습니다!

