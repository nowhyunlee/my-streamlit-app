import streamlit as st

# ใช้ CSS ปรับสไตล์ทุกจุด
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300&family=Sriracha&display=swap');

        .pink-text {
            text-align: center;
            font-size: 22px;
            color: #ff4081;
            font-family: 'Kanit', sans-serif;
        }

        input[type="text"] {
            font-family: 'Kanit', sans-serif;
            font-size: 16px;
            text-align: left;
            color: pink;
        }

        .stButton>button {
            font-family: 'Kanit', sans-serif;
            font-size: 20px;
            color: white;
            background-color: #ff4081;
            border-radius: 12px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ตั้งค่าหน้าเว็บ
st.markdown("<p class='pink-text'>💖 เช็คชื่อของคุณ 💖</p>", unsafe_allow_html=True)

# ช่องกรอกชื่อ
name = st.text_input("🌟", key="name", placeholder="กรุณากรอกชื่อของคุณ")

if name:
    if name in ["เมจิ", "เม", "meiji", "Meiji", "อภิญญา", "Apinya"]:
        st.markdown("<p class='pink-text'> 🪄คุณใช่เมจิเพื่อนของฉันแน่หรือ?! </p>", unsafe_allow_html=True)

        # คำถามรอบที่สอง
        st.markdown("<p class='pink-text'> 🧙เมจิชอบตัวละครใดใน Harry Potter?</p>", unsafe_allow_html=True)
        favemeiji = st.text_input("", key="favemeiji")

        if favemeiji:
            if favemeiji in ["เดรโก", "มัลฟอย", "เดรโก้", "เดรโก มัลฟอย", "Draco", "draco", "draco malfoy", "Draco Malfoy"]:
                st.balloons()
                st.markdown("<p class='pink-text'>💖 เห้ย!! ไอเมเพื่อน💖</p>", unsafe_allow_html=True)
                st.markdown(
                    """
                    <div style="display: flex; justify-content: center;">
                        <img src="https://media1.tenor.com/m/Jx30tRnzLrkAAAAd/malfoy-tom.gif" width="300">
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            else:
                st.markdown("<p class='pink-text'>🤔 เห้ย เอ็งเป็นใครเนี่ย! </p>", unsafe_allow_html=True)

    elif name in ["ไอซ์", "ice", "Ice", "Warunya", "วรัญญา"]:
        st.markdown("<p class='pink-text'> 🪄คุณใช่ไอซ์เพื่อนของฉันแน่หรือ?! </p>", unsafe_allow_html=True)

        # คำถามรอบที่สอง
        st.markdown("<p class='pink-text'> 🧐 ไอซ์ชอบสมาชิกคนใดมากที่สุดในวง NCT?</p>", unsafe_allow_html=True)
        faveice = st.text_input("", key="faveice")

        if faveice:
            if faveice in ["mark", "มาร์ค", "มาร์ค ลี", "Mark", "Mark lee", "Mark Lee"]:
                st.balloons()
                st.markdown("<p class='pink-text'>💖 เห้ย!! ไอซ์จริงด้วย💖</p>", unsafe_allow_html=True)
                st.markdown(
                    """
                    <div style="display: flex; justify-content: center;">
                        <img src="https://64.media.tumblr.com/7da6ae5a4e24dae7708ab1a2b698c3db/tumblr_inline_prny6f7g5P1s2jtnf_540.gifv" width="300">
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            else:
                st.markdown("<p class='pink-text'>🤔 เห้ย เอ็งเป็นใครเนี่ย! </p>", unsafe_allow_html=True)

    elif name in ["บิว", "biw", "Biw", "ชลลดา", "Chonlada"]:
        st.markdown("<p class='pink-text'> 🪄คุณใช่บิวเพื่อนของฉันแน่หรือ?! </p>", unsafe_allow_html=True)

        # คำถามรอบที่สอง
        st.markdown("<p class='pink-text'> 🧐 บิวมีแฟนหนุ่มชื่ออะไร?</p>", unsafe_allow_html=True)
        favebiw = st.text_input("", key="favebiw")

        if favebiw:
            if favebiw in ["เน็ท", "พี่เน็ท", "บ่าว", "Jiranet", "Net"]:
                st.balloons()
                st.markdown("<p class='pink-text'>💖 เห้ย!! บิวเพื่อน มึงจริงด้วย💖</p>", unsafe_allow_html=True)
                st.markdown(
                    """
                    <div style="display: flex; justify-content: center;">
                        <img src="https://i.pinimg.com/originals/e4/c5/6d/e4c56dbf6c64f90a45e1a58e15b9fec3.gif" width="300">
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            else:
                st.markdown("<p class='pink-text'>🤔 เห้ย เอ็งเป็นใครเนี่ย! </p>", unsafe_allow_html=True)

    else:
        st.error("💔 ออกไป!")
