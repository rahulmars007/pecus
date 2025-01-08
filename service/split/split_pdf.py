from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(pdf_path,a,b):
    with open(pdf_path+"/sample.pdf", 'rb') as infile:
        reader = PdfFileReader(infile)
        writer = PdfFileWriter()
        for i in range(a,b+1):
            writer.addPage(reader.getPage(i-1))

        with open(pdf_path+'/split.pdf', 'wb') as outfile:
            writer.write(outfile)