import os

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


def create_page_pdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1, num + 1):
        c.drawString((210 // 2) * mm, (20) * mm, str(i))
        c.showPage()
    c.save()


def add_page_numgers(pdf_path, newpath):
    """
    Add page numbers to a pdf, save the result as a new pdf
    @param pdf_path: path to pdf
    """
    tmp = "__tmp.pdf"

    writer = PdfWriter()
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        n = len(reader.pages)

        # create new PDF with page numbers
        create_page_pdf(n, tmp)

        with open(tmp, "rb") as ftmp:
            number_pdf = PdfReader(ftmp)
            # iterarte pages
            for p in range(n):
                page = reader.pages[p]
                number_layer = number_pdf.pages[p]
                # merge number page with actual page
                page.merge_page(number_layer)
                writer.add_page(page)

            # write result
            if len(writer.pages) > 0:
                with open(newpath, "wb") as f:
                    writer.write(f)
        os.remove(tmp)



add_page_numgers("Filling Time by Kev O'Shea.pdf", "output3.pdf")