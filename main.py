from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    # for header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=30)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], border=0, align="C")
    pdf.line(10, 22, 200, 22)

    # for footer
    pdf.ln(270)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=18, txt=row['Topic'], align="R")
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=18, txt=row['Topic'], align="R")

pdf.output("ProgrammingNotes.pdf")
