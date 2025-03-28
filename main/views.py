from re import search

from django.shortcuts import render, get_object_or_404, redirect

from main.models import *


def mualliflar_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        mualliflar = Muallif.objects.filter(ism__contains=search_query)
    else:
        mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
        'search_param': search_query
    }
    return render(request, 'mualliflar.html', context)


def home_view(request):
    return render(request, 'home.html')


def muallif_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        "muallif": muallif,
    }
    return render(request, 'muallif_details.html', context)

def muallif_post_view(request):
    if request.method=="POST":
        Muallif.objects.create(
            ism=request.POST.get('ism'),
            jins=request.POST.get('jins'),
            tugilgan_sana=request.POST.get('tugilgan_sana') if request.POST.get('tugilgan_sana') else None,
            kitob_soni=request.POST.get('kitob_soni') if request.POST.get('kitob_soni') else None,
            tirk= True if request.POST.get('ism') else False
        )
        return redirect('mualliflar_list')
    return render(request,'muallif_post.html')

def katta_mualliflar(request):
    mualliflar = Muallif.objects.order_by('-tugilgan_sana')
    context = {
        'mualliflar': mualliflar
    }
    return render(request, 'katta_muallif.html', context)

def muallif_delete(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    muallif.delete()
    return redirect('mualliflar_list')

def kitob_soni(request):
    mualliflar=Muallif.objects.order_by('kitob_soni')[:3]
    context={
        'mualliflar':mualliflar
    }
    return render(request,'kitob_soni.html',context)

def tirikmi(request):
    mualliflar=Muallif.objects.filter(tirik=True)
    context={
        'mualliflar':mualliflar,
    }
    return render(request,'tirikmi.html',context)


def kitoblar_view(request):
    kitoblar=Kitob.objects.all()
    context={
        'kitoblar':kitoblar,
    }
    return render(request,'kitoblar.html',context)
def kitob_view(request,kitob_id):
    kitob=Kitob.objects.get(id=kitob_id)
    context={
        'kitob':kitob
    }
    return render(request,'kitob.html',context)



def sahifa_max(request):
    kitoblar=Kitob.objects.order_by('sahifa')[:3]
    context={
        'kitoblar':kitoblar
    }
    return render(request,'sahifa.html',context)



def tirikmlarni_kitobi(request):
    kitoblar=Kitob.objects.filter(muallif__tirik=True)
    context={
        'kitoblar':kitoblar
    }
    return render(request,'tirik_kitob.html',context)

def kitoblar_badiy(request):
    kitoblar=Kitob.objects.filter(janr='badiy')
    context={
        'kitoblar':kitoblar,
    }
    return render(request,'kitoblari.html',context)

def kitoblar(request):
    kitoblar=Kitob.objects.filter(muallif__kitob_soni__lt=10)
    context={
        'kitoblar':kitoblar
    }
    return render(request,'s_kitoblar.html',context)

def adminlar_view(request):
    if request.method=="POST":
        Admin.objects.create(
            ism=request.POST.get('ism'),
            ish_vaqti=Admin.objects.get(id='ish_vaqti')
        )
        return redirect('adminlar')
    adminlar=Admin.objects.all()
    context={
        'adminlar':adminlar
    }
    return render(request,'adminlar.html',context)


def talabalar_view(request):
    if request.method=="POST":
        Talaba.objects.create(
            ism=request.POST.get('ism'),
            guruh=request.POST.get('guruh'),
            kurs=request.POST.get('kurs'),
            kitob_soni=request.POST.get('kitob_soni'),
        )
        return redirect('talabalar_list')
    search_query=request.GET.get('search','')
    if search_query:
        talabalar=Talaba.objects.filter(ism__contains=search_query)
    else:
        talabalar = Talaba.objects.all()
    context = {
        'talabalar': talabalar,
        'search_param':search_query
    }
    return render(request, 'talabalar.html', context)

def talaba_view(request,talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba.html', context)

def talaba_delete(request,talaba_id):
    talaba = get_object_or_404(Talaba,id=talaba_id)
    talaba.delete()
    return redirect('talabalar_list')

def bitiruvchilar(request):
    recordlar=Record.objects.filter(talaba__kurs=4)
    context={
        'recordlar':recordlar
    }
    return render(request,'bitiruvchilar.html',context)



def records_view(request):
    if request.method == "POST":
        Record.objects.create(
            talaba=Talaba.objects.get(id=request.POST.get('talaba_id')),
            kitob=Kitob.objects.get(id=request.POST.get('kitob_id')),
            admin=Admin.objects.get(id=request.POST.get('admin_id')),
            olingan_sana=request.POST.get('olish_sana') if request.POST.get('olish_sana') else None,
            qaytarish_sana=request.POST.get('qaytish_sana') if request.POST.get('qaytish_sana') else None,
        )
        return redirect('recordlar_list')
    search_query = request.GET.get('search', '')
    if search_query:
        recordlar = Record.objects.filter(talaba__ism__icontains=search_query)
    else:
        recordlar = Record.objects.all()
    context = {
        'recordlar': recordlar,
        'search_param': search_query,
        'talabalar':Talaba.objects.all(),
        'kitoblar':Kitob.objects.all(),
        'adminlar':Admin.objects.all()
    }
    return render(request, 'records.html', context)

def record_view(request, pk):
    record = Record.objects.get(pk=pk)
    context = {
        'record':record
    }
    return render(request, 'record_details.html', context)

def last_records(request):
    recordlar=Record.objects.order_by('-olingan_sana')[:3:-1]
    context={
        'recordlar':recordlar
    }
    return render(request,'last_records.html',context)

def record_delete(request, record_id):
    record = Record.objects.get(id=record_id)
    record.delete()
    return redirect('recordlar-list')


