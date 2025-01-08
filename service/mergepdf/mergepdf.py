from PyPDF2 import PdfFileMerger


def merging(path,n):
    pdfs=[]
    for i in range(1,n+1):
        t="sample{}.pdf".format(i)
        pdfs.append(t)
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(path+"/"+pdf)
    merger.write(path+"/"+"result.pdf")
    merger.close()