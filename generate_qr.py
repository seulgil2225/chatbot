"""
mySUNI 챗봇 QR코드 생성 스크립트
배포된 Streamlit 앱 URL을 QR코드로 변환합니다.
"""

import qrcode
from PIL import Image
import os

# ========================================
# 설정: 여기에 Streamlit 앱 URL 입력
# ========================================
CHATBOT_URL = "https://your-app-name.streamlit.app"  # 배포 후 실제 URL로 변경하세요!

# QR코드 설정
qr = qrcode.QRCode(
    version=1,  # 1~40 (숫자가 클수록 QR코드 크기 증가)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # 높은 오류 수정 (로고 삽입 가능)
    box_size=10,  # 각 박스 크기
    border=4,  # 테두리 크기
)

# URL 추가
qr.add_data(CHATBOT_URL)
qr.make(fit=True)

# QR코드 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# 로고 추가 (선택사항)
if os.path.exists("sunny_character.png"):
    try:
        logo = Image.open("sunny_character.png")
        
        # 로고 크기 조정 (QR코드의 1/5 크기)
        qr_width, qr_height = img.size
        logo_size = qr_width // 5
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # 로고를 QR코드 중앙에 배치
        logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        img.paste(logo, logo_pos)
        
        print("✅ 써니 캐릭터 로고가 QR코드에 추가되었습니다!")
    except Exception as e:
        print(f"⚠️ 로고 추가 실패: {e}")
        print("로고 없이 QR코드를 생성합니다.")

# QR코드 저장
output_file = "mysuni_chatbot_qr.png"
img.save(output_file)

print("\n" + "="*50)
print("🎉 QR코드 생성 완료!")
print("="*50)
print(f"📍 저장 위치: {output_file}")
print(f"🔗 연결 URL: {CHATBOT_URL}")
print("\n다음 단계:")
print("1. QR코드를 스캔하여 챗봇 접속 테스트")
print("2. 포스터/명함/스티커에 인쇄하여 배포")
print("3. 사내 포털/메신저에 이미지 첨부")
print("="*50)

# 미리보기 (선택사항)
try:
    img.show()  # 기본 이미지 뷰어로 열기
except:
    print("\n💡 미리보기를 수동으로 확인하세요: mysuni_chatbot_qr.png")

