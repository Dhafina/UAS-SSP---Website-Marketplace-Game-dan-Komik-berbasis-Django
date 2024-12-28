from django.shortcuts import render

def produk(request):
    titelnya="Produk"
    konteks = {
        'titel' : titelnya,
    }
    return render(request,'produk.html',konteks)

# Create your views here.
