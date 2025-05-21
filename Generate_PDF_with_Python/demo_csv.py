from fpdf import FPDF
from fpdf.fonts import FontFace
import csv

with open('D:\inligntech\Generate_PDF_with_Python\credit.csv',encoding='utf-8') as csvfile:
    data = list(csv.reader(csvfile,delimiter=','))
    data = [dat[2:8] for dat in data]
pdf=FPDF()
pdf.set_font("helvetica",size=14)
pdf.add_page()





pdf.set_draw_color(255,0,0)
pdf.set_line_width(0.3)
heading_style = FontFace(emphasis="BOLD",color=255,fill_color=(255,100,0))
with pdf.table(

    borders_layout="NO_HORIZONTAL_LINES",
    cell_fill_color=(224,235,255),
    line_height=6,
    width=160,
    headings_style=heading_style
) as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)
pdf.output('table.pdf')