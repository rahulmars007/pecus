import pdfplumber

def extracttext(path):
    file=open(path + '/sample.txt','w',encoding="utf-8")
    with pdfplumber.open(path + '/sample.pdf') as pdf:
        for page in pdf.pages:
            t=page.extract_text()
            try:
                file.write(t)
            except TypeError:
                continue
