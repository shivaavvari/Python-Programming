from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica","B",size=12) 
        width = self.get_string_width(self.title)+ 6
        self.set_x((210-width)/2)
        self.set_draw_color(0,80,180)
        self.set_fill_color(200,220,255)
        self.set_text_color(220,50,50)
        self.set_line_width(1)
        self.cell(width,9,self.title,new_x="LMARGIN",new_y="NEXT",align="C",fill=True)
        self.ln(10) # line break    

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica","i",size=12)
        self.set_text_color(128)
        self.cell(0,10,f"Page {self.page_no()}",align="C")
        
    def chapter_title(self, num , label):
        self.set_font("helvetica","I",size=12) 
        self.set_fill_color(200,220,255)
        self.cell(0,6,f"chapter {num} : {label}",new_x="LMARGIN",new_y="NEXT",align="L",fill=True)

        
    def chapter_body(self,file_path):
        with open(file_path,"rb") as f:
            txt = f.read().decode("latin-1")
        self.set_font("Times",size=12) 
        self.ln(10)
        self.multi_cell(0,5,txt) 
        self.ln() # line break 
        self.set_font(style="I")
        self.cell(0,5,"(End of excerpt)")


    def print_chapter(self, num, title, file_path):
        self.add_page() # add a new page 
        self.chapter_title(num, title)
        self.chapter_body(file_path)

    


pdf =PDF()
pdf.set_title("100 ways to learning programming")
pdf.set_author("Inlign Technologies")

pdf.print_chapter(1,"GETTING STARTED WITH PROGRAMMING","D:\inligntech\PDF\para.txt")
pdf.print_chapter(2,"WHICH PROGRAMMING LANGUAGE","D:\inligntech\PDF\para.txt")

pdf.output("Sample2.pdf")