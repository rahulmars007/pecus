from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate_pages(pdf_path,result_path,dir):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    if dir=="LEFT":
        angle=-90
    elif dir=="RIGHT":
        angle=90
    elif dir=="":
        angle=0
    else:
        angle=180
    page_1 = pdf_reader.getPage(0).rotateClockwise(angle)
    pdf_writer.addPage(page_1)
    with open(result_path+'/rotate.pdf', 'wb') as fh:
        pdf_writer.write(fh)