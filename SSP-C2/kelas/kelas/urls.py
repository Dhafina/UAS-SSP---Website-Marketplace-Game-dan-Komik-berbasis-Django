"""
URL configuration for kelas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from gudang.views import produk
from dashboard.views import *
from django.conf import settings
from django.conf.urls.static import static

def coba1(request):
    return HttpResponse('Udin Slebew')

def coba2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'home.html' ,konteks)

def comic(request):
    titelnya="comic"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'komik.html' ,konteks)

def order(request):
    titelnya="order"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'Order.html' ,konteks)

def game(request):
    titelnya="game"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'game.html' ,konteks)

def contact(request):
    titelnya="contact"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'Contact.html' ,konteks)
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',coba2),
    # path('utama/',coba2),
    path('produk/',produk),
    path('comic/',comic),
    path('order/',order),
    path('game/',game),
    path('contact/',contact),
    path('addbrg/',tambah_barang),
    path('List/',Barang_View),
    path('add/',tambah_barang),
    path('addbrg/', tambah_barang, name='tambah_barang'),
    path('List/', Barang_View, name='list_barang'),
    path('ubah_msg/<int:id>/', ubah_brg, name='ubah_brg'),
    path('Hapus/<int:name>/', hapus_brg, name='hapus_brg'),
    # 
    path('ubah_msg/<int:id>/', ubah_brg, name='ubah_brg'),
    path('hapus_msg/<int:id>/', hapus_brg, name='hapus_brg'),
    path('jenis/', Jenis_View, name='list_jenis'),  # URL pattern untuk tampil_jenis
    path('addjns/', tambah_jenis, name='tambah_jenis'),  # URL pattern untuk tambah_jenis
    path('ubah/<int:id>/', ubah_jenis, name='ubah_jenis'),
    path('hapus/<int:id>/', hapus_jenis, name='hapus_jenis'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)