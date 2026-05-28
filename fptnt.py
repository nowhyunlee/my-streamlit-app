import streamlit as st
import time
from random import randint

# --- 1. ตั้งค่าหน้าเว็บและ CSS ---
st.set_page_config(page_title="เซียมซีความรัก & เนื้อคู่", page_icon="💖")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500&display=swap');

        * {
            font-family: 'Kanit', sans-serif;
        }

        .title-text {
            text-align: center;
            font-size: 38px;
            font-weight: 500;
            color: #E91E63;
            margin-bottom: 5px;
        }

        .subtitle-text {
            text-align: center;
            font-size: 18px;
            color: #D81B60; 
            margin-bottom: 20px;
        }

        .status-text {
            text-align: center;
            font-size: 20px;
            color: #C2185B;
            font-weight: 500;
        }

        .result-number {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: #E91E63;
            background-color: #FCE4EC;
            border: 3px solid #F48FB1;
            border-radius: 20px;
            padding: 15px;
            margin: 20px 0;
            box-shadow: 0px 4px 10px rgba(233, 30, 99, 0.2);
        }

        .prediction-box {
            font-size: 18px;
            color: #424242;
            background-color: #FAFAFA;
            border-left: 6px solid #F06292;
            padding: 20px;
            margin-top: 10px;
            border-radius: 8px;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        }

        .match-box {
            font-size: 18px;
            color: #424242;
            background-color: #FFF3E0;
            border-left: 6px solid #FF9800;
            padding: 20px;
            margin-top: 15px;
            border-radius: 8px;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
            animation: fadeIn 0.5s;
        }

        .advice-text {
            color: #D81B60;
            font-weight: 500;
            margin-top: 10px;
        }

        /* ปุ่มกดทั่วไป */
        .stButton>button {
            font-size: 22px;
            color: white;
            background-color: #EC407A;
            border: none;
            border-radius: 12px;
            padding: 15px;
            width: 100%;
            transition: 0.3s;
            box-shadow: 0px 4px 6px rgba(236, 64, 122, 0.3);
        }
        .stButton>button:hover {
            background-color: #D81B60;
            transform: translateY(-2px);
        }

        /* ปุ่มดูเนื้อคู่ */
        div.target-btn > div > button {
            background-color: #FF9800 !important;
            box-shadow: 0px 4px 6px rgba(255, 152, 0, 0.3) !important;
        }
        div.target-btn > div > button:hover {
            background-color: #FB8C00 !important;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
""", unsafe_allow_html=True)

# --- 2. ฐานข้อมูลคำทำนายความรัก (15 แบบ) ---
predictions = {
    1: ("เวทมนตร์แห่งการเริ่มต้น (The Magician)", "พลังงานใหม่ๆ กำลังเข้ามา ความรักจะกลับมามีชีวิตชีวาเหมือนเพิ่งจีบกันใหม่ๆ โลกสดใสขึ้นทันตาเห็น", "💡 คำแนะนำ: เปิดใจรับสิ่งดีๆ และมีความสุขกับปัจจุบันให้มากที่สุด"),
    2: ("เงาสะท้อนของกันและกัน (Twin Flames)", "คุณกำลังดึงดูดคนที่มีคลื่นความถี่เดียวกัน คุยกันคลิกอย่างประหลาด มองตาก็รู้ใจแบบไม่ต้องพูดเยอะ", "💡 คำแนะนำ: เป็นตัวของตัวเองให้สุด เพราะคนที่ใช่จะรักในความเรียลของคุณ"),
    3: ("เมฆหมอกพัดผ่านไป (Healing Heart)", "ฟ้าหลังฝนของดวงความรักมาเยือนแล้ว เรื่องไม่สบายใจจะหายไป เหลือไว้แต่ความสบายใจล้วนๆ", "💡 คำแนะนำ: เคลียร์พื้นที่ในหัวใจให้โล่ง เพื่อต้อนรับความรักที่แสนดี"),
    4: ("จังหวะของพรหมลิขิต (Wheel of Fortune)", "ทุกอย่างถูกกำหนดมาแล้วในเวลาที่เหมาะสม จักรวาลกำลังจัดสรรให้มันลงล็อกในจังหวะที่เพอร์เฟกต์ที่สุด", "💡 คำแนะนำ: ปล่อยให้ความรักค่อยๆ เติบโตไปตามธรรมชาติ จะดีที่สุดเลย"),
    5: ("ความรักสว่างไสวดั่งกองไฟ (Fire Element)", "ดวงความรักช่วงนี้ร้อนแรง มีแพสชันสูงปรี๊ด! มีเกณฑ์จะตกหลุมรักแบบหัวปักหัวปำและใจเต้นแรงสุดๆ", "💡 คำแนะนำ: สนุกกับความตื่นเต้นนี้ได้ แต่อย่าลืมดูแลเทคแคร์กันด้วยนะ"),
    6: ("สายน้ำแห่งความผูกพัน (Water Element)", "เน้นไปที่ความรู้สึกผูกพันลึกซึ้ง ความอ่อนโยน และการดูแลเอาใจใส่แบบอบอุ่นหัวใจ", "💡 คำแนะนำ: ความอ่อนหวานและความเห็นอกเห็นใจ คือไม้ตายในการมัดใจ"),
    7: ("ต้นไม้ที่หยั่งรากลึก (Earth Element)", "ความรักของคุณอาจไม่หวือหวาแต่มั่นคงมากๆ เป็นความซื่อสัตย์และการเป็นเซฟโซนให้กันและกัน", "💡 คำแนะนำ: ให้ความสำคัญกับการกระทำและการอยู่เคียงข้างกันในทุกๆ วัน"),
    8: ("สายลมแห่งความเข้าใจ (Air Element)", "กุญแจสำคัญคือ 'การสื่อสาร' คุยด้วยแล้วสบายใจ แลกเปลี่ยนทัศนคติกันได้ทุกเรื่องโดยไม่อึดอัด", "💡 คำแนะนำ: มีอะไรให้พูดคุยกันตรงๆ ด้วยความเข้าใจ ความรักจะยิ่งแน่นแฟ้น"),
    9: ("รักตัวเองก่อนเสมอ (Self-Love 101)", "ยิ่งคุณมีความสุขและดูแลตัวเองดีเท่าไหร่ ออร่าความน่ารักของคุณก็จะยิ่งพุ่งกระจายจนใครๆ ก็หลง", "💡 คำแนะนำ: ไปทำสวย ทำหล่อ กินของอร่อยๆ เพราะคนที่รักตัวเองน่าดึงดูดที่สุด"),
    10: ("ออร่าแห่งความมีเสน่ห์ (Venus Favor)", "ดวงดาวแห่งความรักส่องแสงมาที่คุณเต็มๆ ช่วงนี้มีเสน่ห์ดึงดูดเป็นพิเศษ ใครเห็นเป็นต้องตกหลุมรัก", "💡 คำแนะนำ: บริหารเสน่ห์ให้ดี แล้วเลือกคนที่ทำให้คุณยิ้มได้กว้างที่สุด"),
    11: ("บททดสอบจากดวงดาว (Saturn's Test)", "ความรักอาจมีเรื่องให้ทดสอบใจนิดหน่อย แต่ถ้าจับมือผ่านไปได้ ความสัมพันธ์จะแข็งแกร่งและน่ารักขึ้นอีกสิบเท่า", "💡 คำแนะนำ: จับมือกันให้แน่น ความอดทนและความเชื่อใจคือสิ่งสำคัญ"),
    12: ("เซอร์ไพรส์จากคนไม่คาดคิด (Unexpected Love)", "เตรียมรับความประหลาดใจ! อาจมีคนน่ารักๆ หรือเรื่องราวดีๆ เข้ามาขโมยหัวใจแบบไม่ทันตั้งตัว", "💡 คำแนะนำ: ลองเปิดใจให้กว้าง แล้วจะรู้ว่าความรักมาในรูปแบบที่น่ารักกว่าที่คิด"),
    13: ("ดวงตะวันในใจเธอ (The Sun)", "ความรักที่เรียบง่าย สดใส และเต็มไปด้วยเสียงหัวเราะ เป็นความสัมพันธ์ที่ทำให้อยากตื่นขึ้นมาเจอในทุกๆ วัน", "💡 คำแนะนำ: รักษาพลังงานบวกนี้ไว้ รอยยิ้มของคุณคือสิ่งที่ฮีลใจได้ดีที่สุด"),
    14: ("เสียงกระซิบจากหัวใจ (The Moon's Intuition)", "ถ้าสัญชาตญาณบอกว่า 'คนนี้แหละใช่' ก็แปลว่าใช่จริงๆ เชื่อในความรู้สึกของตัวเองได้เลย", "💡 คำแนะนำ: ฟังเสียงหัวใจตัวเองดู แล้วจะรู้ว่าความสุขที่แท้จริงอยู่ตรงไหน"),
    15: ("จิ๊กซอว์ชิ้นสุดท้าย (The World)", "ความรักที่แสนจะลงตัว เหมือนจิ๊กซอว์ที่ต่อกันได้พอดีเป๊ะ เติมเต็มทุกส่วนในชีวิตให้สมบูรณ์แบบ", "💡 คำแนะนำ: เมื่อเจอความรักที่ดีแล้ว ก็จงดูแลทะนุถนอมกันและกันให้ดีที่สุด")
}

# --- 3. ฐานข้อมูลลักษณะเนื้อคู่ (4 แบบ พิเศษ) ---
match_types = [
    "<b>❄️ น้องหนาว</b><br>เป็นคนปกติน่ารักๆ ที่พร้อมจะตามใจ <b>'พี่มิ้น'</b> ได้เสมอเลย ไม่ว่าพี่มิ้นจะอยากทำอะไร จะไปไหน น้องหนาวคนนี้ก็พร้อมซัพพอร์ตและคอยอยู่เคียงข้าง เป็นความสบายใจให้กันตลอดไปเลยนะ 🥰",
    "<b>🍼 เบบี๋</b><br>อาจจะมีมุมดื้อนิดหน่อย งอแงบ้างให้พอมีสีสัน แต่อย่าให้ถึงเวลาอ้อนเชียวนะ เพราะอ้อนเบบี๋เก่งเป็นที่ 1! ใครเจอมุมขี้อ้อนนี้เข้าไป รับรองว่าใจเหลวเป็นน้ำ แพ้ทางขั้นสุดแน่นอน 🥺💕",
    "<b>🌻 เบ้บ</b><br>คนที่จะคอยอยู่กับเธอในทุกๆ วัน เป็นความอบอุ่นที่ดีที่สุด <i>'คิดถึงนะคะ รักเบ้บน้า'</i> ประโยคสั้นๆ แต่ฮีลใจสุดๆ ที่จะมีให้กันเสมอ แค่มีเบ้บอยู่ด้วย โลกนี้ก็น่าอยู่ขึ้นเยอะเลย ✨",
    "<b>🥟 สาวหมวย</b><br>สาวหมวยแก้มนุ่มยิ้มสวย! มีความขี้เล่น สดใส น่ารักน่าเอ็นดู แอบกวนนิดๆ ให้พอมีรอยยิ้ม เป็นคนที่จะเข้ามาทำให้โลกสว่างไสว อยู่ด้วยแล้วมีแต่เสียงหัวเราะและความสุขในทุกๆ วันเลย 💓"
]

# --- 4. ส่วนควบคุม Session State ---
if "love_number" not in st.session_state:
    st.session_state.love_number = None
if "match_index" not in st.session_state:
    st.session_state.match_index = None
if "show_match" not in st.session_state:
    st.session_state.show_match = False

# --- 5. ส่วนแสดงผลบนเว็บ ---
st.markdown("<div class='title-text'>💖 เซียมซีทำนายรัก & เนื้อคู่ 💖</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>หลับตา ตั้งจิตนึกถึงเรื่องความรัก แล้วกดปุ่มเพื่อรับคำทำนาย</div>", unsafe_allow_html=True)

animation_area = st.empty()
result_area = st.container()

# ปุ่มหลักสำหรับเสี่ยงเซียมซี
if st.button("🌸 กดเพื่อเสี่ยงเซียมซีความรัก"):
    st.session_state.love_number = None
    st.session_state.match_index = None
    st.session_state.show_match = False
    
    with animation_area.container():
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        status_text.markdown("<p class='status-text'>อธิษฐานถึงคนในใจ หรือความรักที่คุณปรารถนา...</p>", unsafe_allow_html=True)
        time.sleep(1)
        
        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.markdown("<p class='status-text'>🎋 กำลังเขย่ากระบอกเซียมซี... แกรก... แกรก...</p>", unsafe_allow_html=True)
            time.sleep(0.01)
            
        status_text.markdown("<p class='status-text'>✨ ไม้เซียมซีแห่งโชคชะตาหล่นลงมาแล้ว! ✨</p>", unsafe_allow_html=True)
        time.sleep(1)
        
        progress_bar.empty()
        status_text.empty()
        
    # สุ่มเลขเซียมซี และ สุ่มเนื้อคู่
    st.session_state.love_number = randint(1, 15)
    st.session_state.match_index = randint(0, 3)

# --- 6. การแสดงผลคำทำนาย ---
if st.session_state.love_number is not None:
    num = st.session_state.love_number
    title, detail, advice = predictions[num]
    match_info = match_types[st.session_state.match_index]
    
    with result_area:
        # แสดงผลใบเซียมซีและคำทำนายหลัก
        st.markdown(f"<div class='result-number'>ใบที่ {num}</div>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class='prediction-box'>
                <h4 style="color: #E91E63; margin-top: 0;">🔮 {title}</h4>
                <p>{detail}</p>
                <div class='advice-text'>{advice}</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("") 
        
        # กล่องสำหรับแสดงแอนิเมชันตอนโหลดหาเนื้อคู่
        match_animation_area = st.empty()
        
        # ปุ่มกดดูเนื้อคู่ (แสดงเมื่อยังไม่ได้กดดู)
        if not st.session_state.show_match:
            st.markdown("<div class='target-btn'>", unsafe_allow_html=True)
            if st.button("🎯 คลิกดูต่อ: คนแบบไหนที่เข้ากับคุณได้ดี?"):
                
                # โหลดแอนิเมชัน "กร้อก ๆ แกร้ก ๆ"
                with match_animation_area.container():
                    status_match = st.empty()
                    progress_match = st.progress(0)
                    
                    status_match.markdown("<p class='status-text' style='color:#FF9800;'>กำลังประมวลผลเนื้อคู่ที่ใช่...</p>", unsafe_allow_html=True)
                    time.sleep(0.5)
                    
                    for i in range(100):
                        progress_match.progress(i + 1)
                        status_match.markdown("<p class='status-text' style='color:#FF9800;'>กร้อก ๆ แกร้ก ๆ ตามหาคนคลั่งรัก...</p>", unsafe_allow_html=True)
                        time.sleep(0.015)
                        
                    status_match.markdown("<p class='status-text' style='color:#FF9800;'>✨ ปิ๊งป่อง! เจอเนื้อคู่ของคุณแล้ว ✨</p>", unsafe_allow_html=True)
                    time.sleep(1)
                    
                    progress_match.empty()
                    status_match.empty()
                
                # ตั้งค่าให้แสดงผลลัพธ์
                st.session_state.show_match = True
                st.rerun()
                
            st.markdown("</div>", unsafe_allow_html=True)
        
        # แสดงข้อมูลลักษณะคนที่เข้ากันได้ดี (แสดงเมื่อกดปุ่มและโหลดเสร็จแล้ว)
        if st.session_state.show_match:
            st.markdown(f"""
                <div class='match-box'>
                    <h4 style="color: #FF9800; margin-top: 0;">👩‍❤️‍👨 เนื้อคู่ที่ใช่สำหรับคุณคือ...</h4>
                    <p>{match_info}</p>
                </div>
            """, unsafe_allow_html=True)
