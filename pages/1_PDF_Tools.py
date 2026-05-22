import streamlit as st
from pypdf import PdfWriter
import io

st.set_page_config(page_title="FileHub - PDF Tools", page_icon="📄")

st.title("📄 أداة دمج ملفات PDF")
st.write("ارفع ملفات PDF الخاصة بك وسأقوم بدمجها لك في ملف واحد احترافي.")

# رفع الملفات
uploaded_files = st.file_uploader("اختر ملفات PDF للدمج", accept_multiple_files=True, type="pdf")

if st.button("دمج الملفات"):
    if uploaded_files:
        writer = PdfWriter()
        for file in uploaded_files:
            writer.append(file)
        
        # حفظ النتيجة في الذاكرة
        output = io.BytesIO()
        writer.write(output)
        
        # زر التحميل
        st.download_button(
            label="تحميل الملف المدمج ⬇️",
            data=output.getvalue(),
            file_name="merged.pdf",
            mime="application/pdf"
        )
        st.success("تم دمج الملفات بنجاح!")
    else:
        st.warning("يرجى رفع ملفات PDF أولاً.")
