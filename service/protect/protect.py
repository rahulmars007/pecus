from PyPDF2 import PdfFileWriter, PdfFileReader

def encryption(input_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf+'/sample.pdf')

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 
                       use_128bit=True)

    with open(input_pdf+'/protect.pdf', 'wb') as fh:
        pdf_writer.write(fh)