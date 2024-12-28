from django.shortcuts import render, get_object_or_404,redirect
from dashboard.forms import FormBarang, FormJenis
from dashboard.models import Barang, Jenis
from django.contrib import messages
# Create your views here.

# def tambah_barang(request):
#     if request.POST:
#         form=FormBarang(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Data Berhasil Ditambahkan")
#             form = FormBarang()
#             konteks = {
#                 'form': form,
#             }
#             return render(request,'tambah_barang.html',konteks)
#     else:
#         form=FormBarang()
#         konteks = {
#             'form':form,
#         }
#     return render(request,'tambah_barang.html',konteks)



# def Barang_View(request):
#     barangs=Barang.objects.all()
#     konteks= {
#         'barangs':barangs
#     }
#     return render(request,'tampil_brg.html',konteks)


def Barang_View(request):
    barangs = Barang.objects.all()
    konteks = {
        'barangs': barangs
    }
    return render(request, 'tampil_brg.html', konteks)

def tambah_barang(request):
    if request.POST:
        form = FormBarang(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks={
                'form':form,
            }
            return render(request,'tambah_barang.html',konteks)
        else:
            messages.error(request, "Data Gagal Ditambahkan. Periksa kembali isian Anda.")
    else:
        form = FormBarang()
    konteks = {
        'form': form,
    }
    return render(request, 'tambah_barang.html', konteks)


def ubah_brg(request, id):
    order = get_object_or_404(Barang, id=id)
    if request.method == 'POST':
        form = FormBarang(request.POST,request.FILES,instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "barang sudah ter edit")
            return redirect('list_barang')
        else:
            messages.error(request, "Terjadi error ; data is invalid.")
    else:
        form = FormBarang(instance=order)
    
    context = {
        'form': form,
        'order': order,
    }
    return render(request, 'ubah_brg.html', context)

def hapus_brg(request, id):
    order = get_object_or_404(Barang, id=id)
    order.delete()
    messages.success(request, "Barang berhasil dihapus")
    # return redirect('/List')
    return redirect('list_barang')

# View untuk menampilkan daftar jenis
def Jenis_View(request):
    jenis = Jenis.objects.all()
    konteks = {
        'jenis': jenis
    }
    return render(request, 'tampil_jenis.html', konteks)

def tambah_jenis(request):
    if request.POST:
        form = FormJenis(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Jenis berhasil ditambahkan")
            return redirect('list_jenis')
        else:
            messages.error(request, "Data gagal ditambahkan. Periksa kembali isian Anda.")
    else:
        form = FormJenis()
    konteks = {
        'form': form,
    }
    return render(request, 'tambah_jenis.html', konteks)

# View untuk mengubah jenis
def ubah_jenis(request, id):
    jenis = get_object_or_404(Jenis, id=id)
    if request.method == 'POST':
        form = FormJenis(request.POST, instance=jenis)
        if form.is_valid():
            form.save()
            messages.success(request, "Jenis berhasil diubah")
            return redirect('list_jenis')
        else:
            messages.error(request, "Data gagal diubah. Periksa kembali isian Anda.")
    else:
        form = FormJenis(instance=jenis)
    
    konteks = {
        'form': form,
        'jenis': jenis,
    }
    return render(request, 'ubah_jns.html', konteks)

# View untuk menghapus jenis
def hapus_jenis(request, id):
    jenis = get_object_or_404(Jenis, id=id)
    jenis.delete()
    messages.success(request, "Jenis berhasil dihapus")
    return redirect('list_jenis')