import streamlit as st

# ฟังก์ชันวาดหัวใจขนาดใหญ่และอยู่กลางจริง ๆ
def draw_heart():
    return """
	<div style="display: flex; justify-content: center; align-items: center;">
		<pre style='font-size: 32px; line-height: 1.2; text-align: center;'>
		❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️			
		</pre>
	</div>
    """

# ใช้ CSS ปรับสไตล์ทุกจุด
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300&family=Sriracha&display=swap');

        /* ปรับฟอนต์และสีของข้อความ */
        .cute-text {
            text-align: center;
            font-size: 26px;
            color: #ff4081;
            font-family: 'Kanit', sans-serif;
        }

        .white-text {
            text-align: center;
            font-size: 22px;
            color: white;
            font-family: 'Kanit', sans-serif;
        }

        /* ปรับฟอนต์ของ input text ให้เหมือนกัน */
        input[type="text"] {
            font-family: 'Kanit', sans-serif;
            font-size: 16px;
            text-align: left;
            color: white !important;
            background-color: black; /* เปลี่ยนสีพื้นหลังให้ตัดกับสีขาว */
            border: 1px solid white; /* เส้นขอบสีขาว */
        }

        /* สำหรับเบราว์เซอร์บางตัวที่อาจไม่รองรับ input[type="text"] */
        .stTextInput>div>div>input {
            color: white !important;
            background-color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# ตั้งค่าหน้าเว็บ
st.markdown("<p class='cute-text'>💖 เช็คชื่อก่อนนะ! 💖</p>", unsafe_allow_html=True)

# ช่องกรอกชื่อ
name = st.text_input( "🌟", key="name", placeholder="กรุณากรอกชื่อของคุณ")

if name:
    if name == "เต็นท์":
        st.markdown("<p class='white-text'>🥰 น้องเต็นท์จริงหรือเปล่าเนี่ย?! </p>", unsafe_allow_html=True)

        # คำถามรอบที่สอง
        st.markdown("<p class='white-text'>🍵 น้องเต็นท์ชอบดื่มอะไรวันละพันแก้ว?</p>", unsafe_allow_html=True)
        fav_drink = st.text_input("", key="fav_drink")

        if fav_drink:  # ตรวจสอบว่ามีอินพุตก่อน
            if fav_drink == "ชาเขียว":
                st.balloons()
                st.markdown("<p class='cute-text'>💖 อ้วน เธอจริงๆ ด้วย! พี่ให้นะคะ 🥺💖</p>", unsafe_allow_html=True)
                st.markdown(draw_heart(), unsafe_allow_html=True)  # แสดงหัวใจตรงกลาง
            else:
                st.markdown("<p class='white-text'>🤔 ไม่ใช่น้า เอาใหม่! </p>", unsafe_allow_html=True)

    else:
        st.error("💔 เฉพาะน้องเต็นท์!")
