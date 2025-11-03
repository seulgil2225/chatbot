# 🔲 QR코드 생성 가이드

Streamlit Cloud 배포가 완료되었으면 이제 QR코드를 만들 수 있습니다!

---

## ✅ 배포 완료 체크리스트

QR코드 생성 전 확인하세요:
- [ ] Streamlit Cloud에 배포 완료
- [ ] 공개 URL 확인 (예: `https://mysuni-chatbot-abc123.streamlit.app`)
- [ ] 브라우저에서 URL 접속 테스트
- [ ] 챗봇이 정상 작동하는지 확인

---

## 방법 1: Python 스크립트 사용

1. **`generate_qr.py` 파일 열기**
   - 메모장 또는 VS Code로 열기

2. **URL 수정**
   ```python
   # 9번째 줄을 찾아서 수정
   CHATBOT_URL = "https://your-app-name.streamlit.app"
   
   # 실제 URL로 변경
   CHATBOT_URL = "https://mysuni-chatbot-abc123.streamlit.app"
   ```

3. **스크립트 실행**
   ```bash
   python generate_qr.py
   ```

4. **QR코드 확인**
   - `mysuni_chatbot_qr.png` 파일이 생성됩니다
   - 파일을 열어서 확인

---

## 방법 2: 온라인 도구 사용 (더 빠름!)

### A. QR Code Generator (가장 간단)
1. https://www.qr-code-generator.com/ 접속
2. "URL" 탭 선택
3. Streamlit 앱 URL 입력
4. "Create QR Code" 클릭
5. "Download" 클릭 (PNG, 300x300 이상)

### B. QRCode Monkey (로고 추가 가능)
1. https://www.qrcode-monkey.com/ 접속
2. "Enter content" 에 URL 입력
3. "Set Colors" 에서 원하는 색상 선택 (선택사항)
4. "Add Logo Image" 에서 `sunny_character.png` 업로드 (선택사항)
5. "Download PNG" 클릭

### C. Canva (디자인 포스터)
1. https://www.canva.com/ 접속
2. "QR Code" 검색
3. 템플릿 선택
4. QR 코드 편집 → URL 입력
5. 포스터 디자인 추가
6. "Download" 클릭

---

## 📱 QR코드 테스트

생성된 QR코드가 제대로 작동하는지 확인:

1. **스마트폰 카메라 앱 실행**
2. **QR코드를 카메라로 비춤**
3. **화면에 URL 팝업 표시 확인**
4. **팝업 클릭 → 챗봇 사이트 접속 확인**
5. **모바일에서 질문 입력 테스트**

✅ 모든 단계가 정상이면 QR코드 사용 준비 완료!

---

## 🖨️ QR코드 인쇄 및 배포

### 인쇄 사이즈 권장
- **포스터**: 최소 10cm x 10cm
- **명함**: 최소 3cm x 3cm
- **스티커**: 최소 5cm x 5cm

### 배포 장소 아이디어
- 총무팀 사무실 입구
- 안내 데스크
- 회의실 입구
- 엘리베이터 안
- 직원 휴게실
- 사내 게시판

---

## 💡 포스터 템플릿 사용

프로젝트에 포함된 `qr_poster_template.html` 파일을 사용하세요:

1. **파일 열기**
   - `qr_poster_template.html` 을 브라우저로 열기

2. **QR코드 이미지 삽입**
   - 개발자 도구(F12)로 편집하거나
   - HTML 에디터에서 QR코드 이미지 경로 수정

3. **인쇄**
   - Ctrl+P (인쇄)
   - "대상"을 "PDF로 저장" 선택
   - 고해상도로 저장

4. **인쇄소에 전달**
   - A4 또는 A3 크기로 출력

---

## 🎉 완료!

이제 누구나 QR코드를 스캔하여 mySUNI 총무 챗봇에 접속할 수 있습니다!

**최종 체크리스트:**
- [ ] QR코드 생성 완료
- [ ] 스마트폰으로 스캔 테스트
- [ ] 모바일에서 챗봇 작동 확인
- [ ] QR코드 인쇄 준비
- [ ] 배포 장소 선정

---

📞 **문의**: 이슬기PM

