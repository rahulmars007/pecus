from docx2pdf import convert
import pythoncom
pythoncom.CoInitialize()
def word_pdf(path_to_upload):
    convert(path_to_upload)