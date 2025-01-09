
from service.rotate.rotate_pdf import rotate_pages
from service.pdftoimage.pdftoimage import pdf_to_image
from service.imagetopdf.image_to_pdf import image_pdf
from service.pdftotext.pdftotext import extracttext
from service.pdftoexcel.pdftoexcel import pdf_excel
from service.protect.protect import encryption
from service.pdftopower.pdf_power import pdf_to_power
from service.pdftoword.pdftoword import pdf_word
from service.mergepdf.mergepdf import merging
from service.split.split_pdf import split_pdf
from service.delete.delete_pdf import delete_pdf
from django.shortcuts import render
from docx2pdf import convert
import string
import random
import os

def home(request):
    return render(request, 'index.html')

def jpgToPdf(request):
    if request.method == "POST":
        # creating random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/jpg2pdf', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        files_list = []
        for file in files.getlist('files'):
            files_list.append(file)
        image_pdf(path_to_upload,files_list)
        return render(request, 'jpgtopdf.html', {'url': str(res)})
    return render(request, 'jpgtopdf.html')

# def pdftojpg(request):
#     # pdf2image
#     if request.method == "POST":
#         # creating random folder name for each user
#         res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
#         path_to_upload = os.path.join('./static/uploaded_files/pdf2jpg', str(res))
#         os.makedirs(path_to_upload)
#         files = request.FILES
#         for file in files.getlist('files'):
#             with open(path_to_upload + '/sample.pdf', 'w+b') as f:
#                 for chunk in file.chunks():
#                     f.write(chunk)
#         pdf_to_image(path_to_upload)
#         return render(request, 'pdftojpg.html', {'url': str(res)})
#     return render(request, 'pdftojpg.html')

def pdftojpg(request):
    if request.method == "POST":
        # Generate a random folder name for each user
        res = ''.join(random.choices(string.ascii_lowercase, k=10))
        path_to_upload = os.path.join('./static/uploaded_files/pdf2jpg', res)
        os.makedirs(path_to_upload, exist_ok=True)

        # Save uploaded files
        uploaded_files = request.FILES.getlist('files')
        if not uploaded_files:
            return render(request, 'pdftojpg.html', {'error': 'No files uploaded!'})

        for file in uploaded_files:
            with open(os.path.join(path_to_upload, 'sample.pdf'), 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        # Convert PDF to images
        try:
            pdf_to_image(path_to_upload)
        except Exception as e:
            return render(request, 'pdftojpg.html', {'error': f'Error processing file: {e}'})

        return render(request, 'pdftojpg.html', {'url': res})

    return render(request, 'pdftojpg.html')

def pdfrotate(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/pdfrotate', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        #print(request.POST.get('id'))
        t=request.POST.get('mars')
        rotate_pages(path_to_upload + '/sample.pdf',path_to_upload,t)
        return render(request, 'pdfrotate.html', {'url': str(res)})
    return render(request, 'pdfrotate.html')

def pdftoexcel(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/pdftoexcel', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        pdf_excel(path_to_upload)
        return render(request, 'pdftoexcel.html', {'url': str(res)})
    return render(request, 'pdftoexcel.html')

def pdftoword(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/pdftoword', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        pdf_word(path_to_upload)
        return render(request, 'pdftoword.html', {'url': str(res)})            
    return render(request,'pdftoword.html')

def pdftopower(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/pdftopower', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        pdf_to_power(path_to_upload + '/sample.pdf')
        return render(request, 'pdftopower.html', {'url': str(res)})
    return render(request,'pdftopower.html')

def pdftotext(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/pdftotext', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        extracttext(path_to_upload)
        return render(request, 'pdftotext.html', {'url': str(res)})
    return render(request,'pdftotext.html')

def wordtopdf(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/wordtopdf', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.docx', 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        convert(path_to_upload + '/sample.docx')
        return render(request, 'wordtopdf.html', {'url': str(res)})            
    return render(request,'wordtopdf.html')

def protect(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/protect', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        data=request.POST.get('pass')
        encryption(path_to_upload,data)
        return render(request, 'protect.html', {'url': str(res)})
    return render(request ,'protect.html')


def merge(request):
    if request.method == "POST":
        # creating random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/merge', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        files_list = []
        c=0
        for file in files.getlist('files'):
            c+=1
            with open(path_to_upload + '/sample{}.pdf'.format(c), 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
                    files_list.append(file)
        merging(path_to_upload,c)
        return render(request, 'merge.html', {'url': str(res)})
    return render(request ,'merge.html')


def split(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/split', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        data=request.POST.get('range')
        t=[]
        for i in data.split(" "):
            t.append(int(i))
        split_pdf(path_to_upload,t[0],t[1])
        return render(request, 'split.html', {'url': str(res)})
    return render(request ,'split.html')


def delete(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/delete', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'w+b') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        data=request.POST.get('range')
        t=[]
        for i in data.split(" "):
            t.append(int(i))
        delete_pdf(path_to_upload,t)
        return render(request, 'delete.html', {'url': str(res)})
    return render(request ,'delete.html')