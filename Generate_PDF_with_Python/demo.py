
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image(r'D:\inligntech\Generate_PDF_with_Python\logo.png', 10, 8, 33)
        self.set_font("helvetica",'B', 16)
        self.cell(80)
        self.cell(40,10,"Hello world",border=1,align="C")
        self.ln(40) # line break
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica",'I', 16)
        self.cell(0,10,f"Page {self.page_no()} / {{nb}} ", align="C")

    
    

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica",'B', 16)
for i in range(1,41):
      pdf.cell(60, 10, f'Printing Line number.{i}', new_x="LMARGIN", new_y="NEXT", align='C')
      #pdf.cell(0,10,f"Printing line number {i}",new_x="LMARGIN", new_y="TOP", align="L")


   
pdf.output("Sample.pdf")