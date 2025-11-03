# 🚀 mySUNI 챗봇 QR코드 사이트 배포 가이드

## 📱 1단계: Streamlit Cloud에 배포하기

### 방법 1: GitHub 연동 (추천)

1. **GitHub 저장소 생성**
   - GitHub에서 새 저장소 생성
   - 로컬 프로젝트를 GitHub에 푸시
   ```bash
   git init
   git add .
   git commit -m "Initial commit: mySUNI chatbot"
   git remote add origin https://github.com/your-username/mysuni-chatbot.git
   git push -u origin main
   ```

2. **Streamlit Cloud 접속**
   - https://share.streamlit.io 방문
   - GitHub 계정으로 로그인

3. **앱 배포**
   - "New app" 클릭
   - Repository: `your-username/mysuni-chatbot`
   - Branch: `main`
   - Main file path: `app.py`
   - "Deploy!" 클릭

4. **환경 변수 설정**
   - 배포된 앱의 Settings > Secrets 이동
   - 다음 내용 입력:
   ```toml
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```
   - Save 클릭

5. **배포 완료!**
   - URL 형식: `https://your-app-name.streamlit.app`
   - 이 URL을 QR코드로 변환하면 됩니다

---

## 🔲 2단계: QR코드 생성하기

### 방법 1: Python 스크립트 사용 (자동화)

```bash
# QR코드 생성 패키지 설치
pip install qrcode[pil]

# QR코드 생성 스크립트 실행
python generate_qr.py
```

생성된 파일: `mysuni_chatbot_qr.png`

### 방법 2: 온라인 도구 사용

1. **QR Code Generator** (무료)
   - https://www.qr-code-generator.com/
   - Streamlit 앱 URL 입력
   - 로고 추가 가능 (sunny_character.png)
   - 고해상도로 다운로드

2. **QRCodeMonkey** (로고 삽입 가능)
   - https://www.qrcode-monkey.com/
   - URL 입력
   - 중앙에 써니 캐릭터 로고 삽입 가능
   - PNG/SVG 다운로드

3. **Canva** (디자인 커스터마이징)
   - https://www.canva.com/
   - QR Code 템플릿 검색
   - 브랜드 색상 및 로고 추가
   - 포스터 형태로 제작 가능

---

## 📋 3단계: QR코드 배포 체크리스트

- [ ] GitHub 저장소 생성 완료
- [ ] Streamlit Cloud 배포 완료
- [ ] Gemini API 키 Secrets 설정 완료
- [ ] 앱 URL 작동 확인 (모바일에서 테스트)
- [ ] QR코드 생성 완료
- [ ] QR코드 스캔 테스트 (실제 스마트폰으로)
- [ ] 챗봇 응답 테스트 (FAQ 질문 3개 이상)

---

## 🎯 4단계: QR코드 활용 방안

### 1. 오프라인 인쇄물
- **포스터**: A4/A3 크기로 사무실 게시판에 부착
- **명함**: 총무팀 명함 뒷면에 인쇄
- **스티커**: 책상, 회의실 입구에 부착

### 2. 디지털 배포
- **이메일 서명**: 총무팀 이메일 서명에 QR코드 추가
- **메신저 프로필**: 카카오톡/슬랙 프로필 이미지
- **사내 포털**: 게시판 공지사항에 첨부

### 3. 안내 문구 예시
```
💻 mySUNI 총무 챗봇
QR코드를 스캔하여 24시간 자동 응답 서비스를 이용하세요!

✅ 임시출입증 발급 방법
✅ 주차등록 절차
✅ 회의실/강의장 예약
✅ 시설 문의

📱 스마트폰으로 QR코드 스캔 → 즉시 질문!
```

---

## 🔧 트러블슈팅

### 문제 1: 앱이 로딩되지 않음
- Streamlit Cloud 대시보드에서 로그 확인
- requirements.txt 패키지 버전 확인
- Python 버전: 3.9 이상 권장

### 문제 2: Gemini API 오류
- Secrets에서 `GEMINI_API_KEY` 정확히 입력했는지 확인
- API 키 할당량 확인: https://makersuite.google.com/
- 키 앞뒤 공백 제거

### 문제 3: FAQ 파일을 찾을 수 없음
- GitHub 저장소에 `mySUNI_FAQ.txt` 파일이 포함되어 있는지 확인
- 파일명 대소문자 정확히 일치하는지 확인

### 문제 4: 모바일에서 UI가 깨짐
- 브라우저 캐시 삭제
- Streamlit Cloud에서 앱 재부팅 (Reboot app)
- `config.toml` 설정 확인

---

## 📞 배포 후 점검사항

1. **기능 테스트**
   - [ ] 모바일 Chrome/Safari에서 접속
   - [ ] 질문 입력 및 답변 확인
   - [ ] 대화 내역 누적 확인
   - [ ] 이미지 (써니 캐릭터) 표시 확인

2. **성능 테스트**
   - [ ] 초기 로딩 속도 (3초 이내)
   - [ ] 답변 생성 속도 (5초 이내)
   - [ ] 여러 사용자 동시 접속 테스트

3. **보안 확인**
   - [ ] API 키가 코드에 노출되지 않음
   - [ ] Secrets에만 저장됨
   - [ ] `.env` 파일이 GitHub에 푸시되지 않음 (.gitignore 확인)

---

## 🎉 완료!

배포가 완료되었습니다! 이제 QR코드를 스캔하여 언제 어디서나 mySUNI 총무 챗봇을 이용할 수 있습니다.

**최종 URL**: `https://your-app-name.streamlit.app`
**QR코드**: `mysuni_chatbot_qr.png`

궁금한 점이 있으면 이슬기PM에게 문의하세요.

