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
        st.session_state.number = randint(1, 9)

    st.markdown(f"<p class='result-box'>🔮 คุณได้เซียมซีหมายเลข {st.session_state.number} 🔮</p>", unsafe_allow_html=True)

    if "show_prediction" not in st.session_state:
        st.session_state.show_prediction = False

    if not st.session_state.show_prediction:
        if st.button("ดูคำทำนาย"):
            st.session_state.show_prediction = True  # กดแล้วแสดงผลและทำให้ปุ่มหายไป

    if st.session_state.show_prediction:
        messages = {
            1: ("💖 รักนี้สดใส หัวใจพองโต 💖", "ความรักของคุณกำลังไปได้ดี อบอุ่นเหมือนแสงแดดอ่อนๆในยามเช้า ถ้ายังโสด มีโอกาสได้พบคนที่ใช่เร็วๆ นี้!"),
            2: ("🌬️ สายลมแห่งรักพัดผ่านมา 🌬️", "ใครบางคนเริ่มแอบมองคุณอยู่ไกลๆ ลองเปิดใจให้โอกาสตัวเองนะ ความรักอาจมาแบบไม่คาดคิด!"),
            3: ("📍 รักแท้ไม่แพ้ระยะทาง 📍", "แม้จะอยู่ไกลกัน แต่ความรู้สึกยังมั่นคง เชื่อมั่นในกันและกัน แล้วทุกอย่างจะราบรื่นไปด้วยดี"),
            4: ("💘 เสี่ยงเซียมซีมาเจอรักแท้ 💘", "เซียมซีใบนี้บอกว่า โชคชะตากำลังจะพาคุณไปพบกับคนที่ทำให้หัวใจเต้นแรง เตรียมตัวให้ดีนะ!"),
            5: ("🎁 รักนี้มีเซอร์ไพรส์ 🎁", "ใครบางคนกำลังคิดจะทำอะไรพิเศษให้คุณ ไม่แน่ว่าอาจมีของขวัญ หรือคำบอกรักที่คุณรอคอย!"),
            6: ("🚀 ดวงความรักพุ่งแรงเวอร์ 🚀", "คนโสดมีเกณฑ์จะมีคนเข้ามาจีบ ส่วนคนมีคู่ ความสัมพันธ์จะยิ่งแน่นแฟ้นขึ้นกว่าเดิม!"),
            7: ("💡 ใจตรงกัน สัญญาณรักมาแล้ว 💡", "ถ้ากำลังลังเลอยู่ ลองส่งสัญญาณไปดู เพราะมีโอกาสสูงมากที่เขาก็รู้สึกเหมือนกัน!"),
            8: ("🧋 ความรักเหมือนชาไข่มุก 🧋", "อดใจรออีกนิด อย่ารีบร้อน เพราะรักที่ดีจะมาหาในเวลาที่เหมาะสม แล้วคุณจะรู้ว่ามันคุ้มค่าที่สุด!"),
            9: ("🔍 หัวใจตรงกัน แอบรักไม่ไกลเกินเอื้อม 🔍", "มีใครบางคนคิดถึงคุณอยู่ อาจเป็นคนใกล้ตัวที่คุณไม่ทันสังเกต ลองสังเกตดูสิ!"),
        }

        title, description = messages[st.session_state.number]
        st.markdown(f"<p class='result-box'>{title}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='pink-text'>{description}</p>", unsafe_allow_html=True)

elif answer.lower() == "no":
    st.markdown("<p class='result-box'>😌 คุณเลือกที่จะไม่เสี่ยงเซียมซี</p>", unsafe_allow_html=True)

elif answer:
    st.markdown("<p class='result-box'>⚠️ กรุณาพิมพ์ yes หรือ no เท่านั้น ⚠️</p>", unsafe_allow_html=True)
