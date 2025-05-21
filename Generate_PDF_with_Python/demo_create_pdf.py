from fpdf import FPDF, XPos,YPos
from pathlib import Path 
class PDF(FPDF):
    def header(self):
        self.image(r'D:\inligntech\Generate_PDF_with_Python\image.jpg', 10, 8, 33)
        self.set_font("helvetica",'B', 16)
        self.cell(80)
        self.cell(90,10,"Python Programming Projects",border=1,align="C")
        self.ln(40) # line break
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica",'I', 16)
        self.cell(0,10,f"Page {self.page_no()} / {{nb}} ", align="C")

    def chapter_title(self,num, label):
        self.set_font("helvetica",'B', 16)
        self.set_fill_color(200,220,255)
        self.cell(0,10,f"Chapter {num}:{label}",0,new_x=XPos.LMARGIN,new_y=YPos.NEXT,align="L",fill=True)
        self.ln(10) 
    
    def chapter_body(self, body):
        self.set_font("helvetica",'I', 16)
        self.multi_cell(0,10,body)  
        self.ln(10)
    

pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica",'B', 16)
pdf.add_page()
pdf.set_font("helvetica",'B', 16)
pth = Path('D:\inligntech')
count=1
for dir in  pth.iterdir():
    if dir.is_dir() and dir.name != '.git':
      pdf.chapter_title(count,dir.name)
      for file in dir.iterdir():
          cnt=1
          if file.is_file() and file.name.endswith('.py'):
                pdf.chapter_title(cnt,file.name)
                cnt+=1
      count+=1

   
pdf.output("Sample.pdf")