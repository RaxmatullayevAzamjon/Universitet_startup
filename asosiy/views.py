from django.shortcuts import render, redirect
from.models import *

def bosh_sahifa(requests):
    return render(requests,'bosh_sahifa.html')

def ustozlar(requests):
    if requests.method == "POST":
        Ustoz.objects.create(
            ism=requests.POST.get("i"),
            jins=requests.POST.get("j"),
            yosh=requests.POST.get("y"),
            daraja=requests.POST.get("d"),
            fan=Fan.objects.get(id=requests.POST.get("f"))
        )
        return redirect("/ustozlar/")
    qidiruv_sozi = requests.GET.get("ism")
    if qidiruv_sozi:
        natija = Ustoz.objects.filter(ism__contains=qidiruv_sozi)
    else:
        natija = Ustoz.objects.all()
    content = {
        "ustozlar": natija,
        "fanlar": Fan.objects.all()
    }
    return render(requests,"hamma_ustozlar.html",content)

def ustoz_update(request, son):
    if request.method == "POST":
        Ustoz.objects.filter(id=son).update(
            yosh=request.POST.get("y"),
            daraja=request.POST.get("d"),
            fan=request.POST.get("f")
        )
        return redirect("/ustozlar/")
    content = {
        "ustoz":Ustoz.objects.get(id=son),
        "fanlar": Fan.objects.all()

    }
    return render(request,"ustoz_update.html",content)


def ustoz_ochir(requests,son):
    Ustoz.objects.get(id=son).delete()
    return redirect("/ustozlar/")

def fan(request):
    if request.method == "POST":
        Fan.objects.create(
            nom=request.POST.get("n"),
            yonalish=Yonalish.objects.get(id=request.POST.get("y")),
            asosiy=request.POST.get("a")
        )
        return redirect("/fanlar/")
    qidiruv_soz = request.GET.get("nom")
    if qidiruv_soz:
        natija = Fan.objects.filter(nom__contains=qidiruv_soz)
    else:
        natija = Fan.objects.all()
    content = {
    "fanlar": natija,
    "yonalishlar": Yonalish.objects.all()

    }
    return render(request,"fanlar.html",content)

def fan_ochir(request, son):
    Fan.objects.get(id=son).delete()
    return redirect("/fanlar/")

def fan_update(request, son):
    if request.method == "POST":
        Fan.objects.filter(id=son).update(
            nom=request.POST.get("n"),
            yonalish=request.POST.get("y"),
            asosiy=request.POST.get("a")
        )
        return redirect("/fanlar/")
    content = {
        "fan": Fan.objects.get(id=son),
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request,"fan_update.html",content)



def yonalish(request):
    if request.method == "POST":
        Yonalish.objects.create(
            nom=request.POST.get("n"),
            aktiv=request.POST.get("a")
        )
        return redirect("/yonalish/")
    content = {
        "yonalishlar":Yonalish.objects.all()
    }
    return render(request,"yonalish.html",content)

def yonalish_ochir(request, son):
    Yonalish.objects.get(id=son).delete()
    return redirect("/yonalish/")

def yonalish_update(request, son):
    if request.method == "POST":
        Yonalish.objects.filter(id=son).update(
            nom=request.POST.get('n'),
            aktiv=request.POST.get('a')
        )
        return redirect("/yonalish/")
    content = {
        "yonalish": Yonalish.objects.get(id=son)
    }
    return render(request,"yonalish_update.html",content)
