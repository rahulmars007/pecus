import img2pdf

def image_pdf(path_to_upload,files_list):
    a4inpt = (img2pdf.mm_to_pt(180), img2pdf.mm_to_pt(250))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    with open(path_to_upload + "/sample.pdf", "wb") as f:
        f.write(img2pdf.convert(files_list, layout_fun=layout_fun))
        