import streamlit as st

# إعدادات عنوان التطبيق في المتصفح
st.set_page_config(page_title="درس القارات والمحيطات", page_icon="🌍", layout="centered")

# --- إضافة خلفية وديزاين مخصص (CSS) ---
st.markdown("""
    <style>
    /* خلفية التطبيق كاملة بلون أزرق سماوي هادئ يليق بالمحيطات */
    .stApp {
        background-color: #e6f2ff;
    }
    
    /* تصميم العناوين الرئيسية */
    h1 {
        color: #1e3d59;
        text-align: center;
        font-family: 'Cairo', sans-serif;
    }
    h3 {
        color: #17b978;
        font-family: 'Cairo', sans-serif;
    }
    
    /* تصميم بطاقات مخصصة لكل سؤال خلفية بيضاء مع إطار دائري وظل */
    .question-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        border-right: 8px solid #17b978; /* خط أخضر جانبي يرمز لليابسة */
    }
    </style>
""", unsafe_allow_html=True)

# عنوان الدرس
st.markdown("<h1>🌍 درس القارات وتعريفها</h1>", unsafe_allowed_html=True)
st.markdown("<h4 style='text-align: center; color: #555;'>الصف الثاني الابتدائي</h4>", unsafe_allowed_html=True)
st.write("---")

# السؤال الأول داخل بطاقة تصميم
st.markdown('<div class="question-box">', unsafe_allowed_html=True)
st.markdown("### **السؤال 1**")
q1 = st.radio(
    "كم عدد قارات العالم ؟",
    ["5 قارات", "6 قارات", "7 قارات"],
    index=None,
    key="q1"
)
st.markdown('</div>', unsafe_allowed_html=True)

# السؤال الثاني داخل بطاقة تصميم
st.markdown('<div class="question-box" style="border-right: 8px solid #1e3d59;">', unsafe_allowed_html=True) # خط أزرق للمحيطات
st.markdown("### **السؤال 2**")
q2 = st.radio(
    "كم عدد محيطات العالم ؟",
    ["4 محيطات", "5 محيطات", "6 محيطات"],
    index=None,
    key="q2"
)
st.markdown('</div>', unsafe_allowed_html=True)

# السؤال الثالث داخل بطاقة تصميم
st.markdown('<div class="question-box">', unsafe_allowed_html=True)
st.markdown("### **السؤال 3**")
q3 = st.radio(
    "في أي قارة يقع الأردن ؟",
    ["قارة أفريقيا", "قارة آسيا", "قارة أوروبا"],
    index=None,
    key="q3"
)
st.markdown('</div>', unsafe_allowed_html=True)

# السؤال الرابع داخل بطاقة تصميم
st.markdown('<div class="question-box">', unsafe_allowed_html=True)
st.markdown("### **السؤال 4**")
q4 = st.radio(
    "ما هو تعريف القارة ؟",
    [
        "أرض صغيرة تحيط بها المياه من كل جانب", 
        "مساحة كبيرة جداً من اليابسة تضم عدداً من الدول", 
        "تجمع كبير من المياه المالحة"
    ],
    index=None,
    key="q4"
)
st.markdown('</div>', unsafe_allowed_html=True)

st.write("---")

# زر تصحيح الإجابات بتصميم مميز
if st.button("اضغط هنا لتصحيح الإجابات ورؤية النتيجة 🎯", use_container_width=True):
    if q1 is None or q2 is None or q3 is None or q4 is None:
        st.warning("الرجاء الإجابة على جميع الأسئلة أولاً! ⚠️")
    else:
        score = 0
        if q1 == "7 قارات": score += 1
        if q2 == "5 محيطات": score += 1
        if q3 == "قارة آسيا": score += 1
        if q4 == "مساحة كبيرة جداً من اليابسة تضم عدداً من الدول": score += 1
            
        st.balloons() 
        st.success(f"🎉 أحسنت يا بطل! درجتك هي: {score} من 4")
        st.write("")
        st.info("💡 مع تحيات معلمة المادة: **كوثر البديرات**")
