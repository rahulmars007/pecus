import fitz   

def delete_pdf(path,n):
    doc = fitz.open(path+"/sample.pdf")             
    l = list(range(doc.pageCount))          
    for i in range(n[0],n[1]+1):
            l.remove(i-1)                     
    doc.select(l)                           
    doc.save(path+"/after-deleted.pdf", garbage=3)         
    doc.close()