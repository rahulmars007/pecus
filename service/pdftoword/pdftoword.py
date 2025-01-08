from docx2pdf import convert
from pdf2docx import Converter

def pdf_word(path_to_upload):
    pdf_file=path_to_upload + '/sample.pdf'
    docx_file=path_to_upload + '/sample.docx'
    cv=Converter(pdf_file)
    cv.convert(docx_file,start=0, end=None)
    cv.close()