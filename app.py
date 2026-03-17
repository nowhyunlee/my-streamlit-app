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
    if name == "เฮีย":
        st.markdown("<p class='white-text'> เฮียจริงไหมครับ? </p>", unsafe_allow_html=True)

        # คำถามรอบที่สอง
        st.markdown("<p class='white-text'> ชื่อของผมคืออะไรครับ?</p>", unsafe_allow_html=True)
        fav_drink = st.text_input("", key="fav_drink")

        if fav_drink:  # ตรวจสอบว่ามีอินพุตก่อน
            if fav_drink == "ชลลี่":
                st.balloons()
                st.markdown("<p class='cute-text'>💖 เฮียจริง ๆ หรอคะ 🥺💖</p>", unsafe_allow_html=True)
                st.markdown(draw_heart(), unsafe_allow_html=True)  # แสดงหัวใจตรงกลาง
            else:
                st.markdown("<p class='white-text'>🤔 ไม่ใช่ครับ เอาใหม่ </p>", unsafe_allow_html=True)

    else:
        st.error("💔 เฮียเท่านั้นครับ")
