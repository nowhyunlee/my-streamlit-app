import streamlit as st
from random import randint

# เพิ่ม CSS ปรับสไตล์ให้ปุ่มและข้อความเข้ากับธีม
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300&display=swap');

        .pink-text {
            text-align: center;
            font-size: 22px;
            color: #ff4081;
            font-family: 'Kanit', sans-serif;
        }
        .p2-text {
            text-align: left;
            font-size: 22px;
            color: #ff4081;
            font-family: 'Kanit', sans-serif;
        }
        .stTextInput>div>div>input {
            font-family: 'Kanit', sans-serif;
            font-size: 16px;
            color: #ff4081;
            text-align: center;
        }

        .stButton>button {
            font-family: 'Kanit', sans-serif;
            font-size: 20px;
            color: white;
            background-color: #ff4081;
            border-radius: 12px;
            padding: 10px;
            width: 100%;
            transition: 0.3s;
        }

        .stButton>button:hover {
            background-color: #d81b60;
        }

        .result-box {
            font-family: 'Kanit', sans-serif;
            font-size: 18px;
            text-align: center;
            color: #ff4081;
            background-color: #ffe6eb;
            padding: 10px;
            border-radius: 10px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='pink-text'>🧧 ยินดีต้อนรับเข้าสู่การเสี่ยงเซียมซี 🧧</p>", unsafe_allow_html=True)
st.markdown("<p class='p2-text'>คุณต้องการที่จะเสี่ยงเซียมซีไหม? (yes/no)</p>", unsafe_allow_html=True)

answer = st.text_input(" ", key="answer", placeholder="พิมพ์ yes หรือ no แล้วกด Enter")

if answer.lower() == "yes":
    if "number" not in st.session_state:
        st.session_state.number = randint(1, 5)

    st.markdown(f"<p class='result-box'>🔮 คุณได้เซียมซีหมายเลข {st.session_state.number} 🔮</p>", unsafe_allow_html=True)

    if "show_prediction" not in st.session_state:
        st.session_state.show_prediction = False

    if not st.session_state.show_prediction:
        if st.button("ดูคำทำนาย"):
            st.session_state.show_prediction = True  # กดแล้วแสดงผลและทำให้ปุ่มหายไป

    if st.session_state.show_prediction:
        messages = {
            1: ("💖 วันนี้วันเกิดใครน้าา 💖", "สุขสันต์วันเกิดนะยะ! ขอให้มีความสุขที่สุดในโลกกก"),
            2: ("💝 ใบนี้แรร์ไอเทม 💝", "สุขสันต์วันเกิดเธออีกรอบน้าา  อยู่เป็นเกรุกที่ตลกให้ชั้นไปนานนานนนนน (ไม่ต้อง) จากน้องหนาวคนสวยของเธอค่ะ 💖"),
            3: ("📍 ปักหมุดวันเกิด 📍", "ดีนะเนี่ยที่เธอเกิดวันนี้ ถ้าเกิด 29 กุมภาไม่ได้ฉลองสักกะทีเลย!"),
            4: ("💘 เซียมซีวันเกิด! 💘", "เซียมซีใบนี้บอกว่า วันนี้เป็นวันเกิดของคุณ! รู้เรื่องป่าวเนี่ย?!"),
            5: ("🎁 เซอร์ไพรส์! 🎁", "อายุ 30 แล้ว! 555555555 ขอให้สุขภาพแข็งแรงมาเตะกับช้านได้😼"),
        }

        title, description = messages[st.session_state.number]
        st.markdown(f"<p class='result-box'>{title}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='pink-text'>{description}</p>", unsafe_allow_html=True)

elif answer.lower() == "no":
    st.markdown("<p class='result-box'>😌 คุณเลือกที่จะไม่เสี่ยงเซียมซี</p>", unsafe_allow_html=True)

elif answer:
    st.markdown("<p class='result-box'>⚠️ กรุณาพิมพ์ yes หรือ no เท่านั้น ⚠️</p>", unsafe_allow_html=True)
