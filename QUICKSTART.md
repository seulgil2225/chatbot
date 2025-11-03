# ⚡ 빠른 시작: QR코드 챗봇 배포하기

10분 안에 mySUNI 챗봇을 QR코드 사이트로 배포하는 방법입니다.

---

## 📋 준비물 체크리스트

- [ ] GitHub 계정
- [ ] Gemini API 키 ([여기서 발급](https://makersuite.google.com/app/apikey))
- [ ] Git 설치 완료
- [ ] Python 3.9+ 설치 완료

---

## 🚀 3단계 배포 프로세스

### 1️⃣ GitHub에 코드 업로드 (2분)

```bash
# 1. Git 초기화
git init

# 2. 모든 파일 추가
git add .

# 3. 첫 커밋
git commit -m "Initial commit: mySUNI chatbot for QR deployment"

# 4. GitHub 저장소 연결 (본인 계정으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/mysuni-chatbot.git

# 5. 푸시
git push -u origin main
```

> ⚠️ **주의**: `.env` 파일은 자동으로 제외됩니다 (.gitignore에 설정됨)

---

### 2️⃣ Streamlit Cloud 배포 (5분)

#### A. 계정 생성 및 로그인
1. https://share.streamlit.io 접속
2. "Sign up with GitHub" 클릭
3. GitHub 권한 승인

#### B. 앱 배포
1. **"New app"** 버튼 클릭
2. 설정 입력:
   - **Repository**: `YOUR_USERNAME/mysuni-chatbot`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. **"Deploy!"** 클릭
4. 2-3분 대기 (자동 배포 진행)

#### C. API 키 설정
1. 배포된 앱 우측 상단 **☰ > Settings** 클릭
2. **Secrets** 탭 선택
3. 다음 내용 입력:
```toml
GEMINI_API_KEY = "여기에_실제_API_키_입력"
```
4. **"Save"** 클릭
5. 앱 자동 재시작 (10초 대기)

#### D. 작동 확인
✅ 챗봇이 정상 작동하는지 테스트 질문:
- "주차등록 어떻게 해요?"
- "임시출입증 발급 방법 알려주세요"

---

### 3️⃣ QR코드 생성 및 배포 (3분)

#### A. URL 확인
배포된 앱 URL 형식:
```
https://YOUR_USERNAME-mysuni-chatbot-app-RANDOM.streamlit.app
```
예시: `https://mysuni-chatbot-abc123.streamlit.app`

#### B. QR코드 생성

**방법 1: Python 스크립트 (추천)**
```bash
# 1. generate_qr.py 파일 열기
# 2. CHATBOT_URL 변수를 실제 URL로 변경
# 3. 실행
python generate_qr.py
```

**방법 2: 온라인 도구 (빠름)**
1. https://www.qr-code-generator.com/ 접속
2. URL 입력
3. "Create QR Code" 클릭
4. 다운로드 (PNG, 최소 300x300px)

#### C. QR코드 테스트
1. 스마트폰 카메라 앱 실행
2. QR코드 스캔
3. 챗봇 사이트 자동 접속 확인
4. 모바일에서 질문 입력 테스트

---

## 📱 QR코드 활용 아이디어

### 1. 인쇄물 제작
- **A4 포스터**: `qr_poster_template.html` 열어서 인쇄
- **명함 크기 스티커**: 복사기 라벨지 사용
- **책상 텐트**: 양면 인쇄 후 접기

### 2. 디지털 배포
- 카카오톡/슬랙 채널에 이미지 공유
- 이메일 서명에 QR코드 삽입
- 사내 포털 게시판에 공지

---

## 🎯 배포 후 체크리스트

완료된 항목에 체크하세요:

- [ ] Streamlit Cloud 배포 완료
- [ ] 브라우저에서 챗봇 접속 확인
- [ ] Gemini API 키 Secrets 설정
- [ ] 챗봇 응답 정상 작동 확인
- [ ] QR코드 생성 완료
- [ ] 스마트폰으로 QR코드 스캔 테스트
- [ ] 모바일 UI 정상 표시 확인
- [ ] QR코드 포스터 인쇄
- [ ] 사무실 게시판에 부착

---

## 🔧 자주 발생하는 오류 해결

### 오류 1: "ModuleNotFoundError: No module named 'dotenv'"
**해결**: Streamlit Cloud는 `requirements.txt`를 자동으로 읽습니다. 파일이 GitHub에 포함되어 있는지 확인하세요.

### 오류 2: "API key not found"
**해결**: Streamlit Cloud Settings > Secrets에서 `GEMINI_API_KEY`를 정확히 입력했는지 확인하세요. 키 앞뒤 공백이 없어야 합니다.

### 오류 3: "File not found: mySUNI_FAQ.txt"
**해결**: GitHub 저장소에 `mySUNI_FAQ.txt` 파일이 포함되어 있는지 확인하세요.

### 오류 4: 모바일에서 UI가 깨짐
**해결**: 브라우저 캐시를 삭제하고 새로고침하세요. 또는 Streamlit Cloud에서 "Reboot app"을 클릭하세요.

---

## 💡 다음 단계

✅ 배포 완료! 이제 다음을 고려하세요:

1. **FAQ 확장**: `mySUNI_FAQ.txt`에 질문 추가
2. **사용 분석**: Streamlit Cloud Analytics 확인
3. **피드백 수집**: 사용자 의견 반영
4. **기능 개선**: 이미지 첨부, 파일 다운로드 등

---

## 📞 도움이 필요하신가요?

- **상세 가이드**: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **기술 문서**: [README.md](README.md)
- **총무 담당**: 이슬기PM

---

**🎉 축하합니다! QR코드 챗봇 배포가 완료되었습니다!**

이제 누구나 QR코드를 스캔하여 24시간 총무 업무 자동 응답 서비스를 이용할 수 있습니다.

