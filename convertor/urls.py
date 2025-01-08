from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('jpgtopdf', views.jpgToPdf),
    path('pdftojpg', views.pdftojpg),
    path('pdfrotate', views.pdfrotate ),
    path('pdftoexcel',views.pdftoexcel),
    path('pdftoword',views.pdftoword),
    path('pdftopower',views.pdftopower),
    path('pdftotext',views.pdftotext),
    path('wordtopdf',views.wordtopdf),
    path('protect',views.protect),
    path('merge',views.merge),
    path('split',views.split),
    path('delete',views.delete),

]