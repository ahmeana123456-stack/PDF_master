from fpdf import FPDF

# إنشاء ملف PDF يحتوي على جدول بسيط
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="جدول بيانات تجريبي لمشروع PDF-to-Excel Master", ln=True, align='C')
pdf.cell(200, 10, txt="الاسم | العمر | المهنة", ln=True, align='C')
pdf.cell(200, 10, txt="---------------------------------------", ln=True, align='C')
pdf.cell(200, 10, txt="احمد | 25 | مبرمج", ln=True, align='C')
pdf.cell(200, 10, txt="سارة | 30 | مهندسة", ln=True, align='C')
pdf.output("test_table.pdf")
print("تم إنشاء ملف 'test_table.pdf' بنجاح في المجلد!")