from PyPDF2 import PdfWriter, PdfReader

def encryption(input_pdf, password):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(input_pdf+'/sample.pdf')

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(user_password=password, owner_password=None, 
                       use_128bit=True)

    with open(input_pdf+'/protect.pdf', 'wb') as fh:
        pdf_writer.write(fh)