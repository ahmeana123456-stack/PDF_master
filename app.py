import streamlit as st
import pdfplumber
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from gtts import gTTS

# إعدادات الصفحة
st.set_page_config(page_title="المحول الشامل", layout="wide")
st.title("🔀 المحول الشامل للبيانات والوسائط")

# تقسيم الموقع لتبويبات
tab1, tab2 = st.tabs(["📂 ملفات (PDF/Excel)", "🎙️ أدوات الصوت"])

# --- التبويب الأول: الأدوات القديمة ---
with tab1:
    uploaded_file = st.file_uploader("ارفع ملفك هنا (PDF أو Excel)", type=["pdf", "xlsx"])
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            if st.button("تحويل PDF إلى Excel"):
                with pdfplumber.open(uploaded_file) as pdf:
                    all_data = []
                    for page in pdf.pages:
                        table = page.extract_table()
                        if table: all_data.extend(table)
                    if all_data:
                        df = pd.DataFrame(all_data)
                        buffer = io.BytesIO()
                        df.to_excel(buffer, index=False)
                        st.download_button("تحميل ملف Excel", buffer.getvalue(), "converted.xlsx")
                        st.success("تم التحويل بنجاح!")
                    else: st.error("لم يتم العثور على جداول.")

        elif uploaded_file.name.endswith(".xlsx"):
            if st.button("تحويل Excel إلى PDF"):
                df = pd.read_excel(uploaded_file)
                buffer = io.BytesIO()
                c = canvas.Canvas(buffer, pagesize=letter)
                text_y = 750
                for index, row in df.iterrows():
                    c.drawString(50, text_y, str(row.tolist()))
                    text_y -= 20
                    if text_y < 50: c.showPage(); text_y = 750
                c.save()
                st.download_button("تحميل ملف PDF", buffer.getvalue(), "converted.pdf")
                st.success("تم التحويل بنجاح!")

# --- التبويب الثاني: الأدوات الجديدة (الصوت) ---
with tab2:
    st.header("تحويل النص إلى صوت")
    text_input = st.text_area("اكتب النص هنا:")
    if st.button("تحويل إلى صوت"):
        if text_input:
            tts = gTTS(text=text_input, lang='ar')
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            st.audio(audio_buffer.getvalue(), format='audio/mp3')
            st.download_button("تحميل الملف الصوتي", audio_buffer.getvalue(), "output.mp3")
        else: st.warning("يرجى كتابة نص أولاً!")