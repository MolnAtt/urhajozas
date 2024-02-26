from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Urhajos, Kuldetes
from datetime import date

@login_required
def feltoltes_view(request):
    template = 'feltoltes.html'
    context = {}
    return render(request, template, context)


@login_required
def urhajos_feltoltese_view(request):
    template = 'feltoltes_urhajos.html'
    context = {}
    return render(request, template, context)


@login_required
def urhajos_feltoltese_view_kuld(request):
    template = 'feltoltes_urhajos_kuld.html'
    context = {}
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')
    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        Urhajos.objects.create(
            az=int(sortomb[0]),
            nev=sortomb[1],
            orszag=sortomb[2],
            nem=sortomb[3],
            szulev=int(sortomb[4]),
            urido=sortomb[5],
        )

    return render(request, template, context)




@login_required
def kuldetes_feltoltese_view(request):
    template = 'feltoltes_kuldetes.html'
    context = {}
    return render(request, template, context)


@login_required
def kuldetes_feltoltese_view_kuld(request):
    template = 'feltoltes_kuldetes_kuld.html'
    context = {}
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')

    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        kezdetstrtomb = sortomb[2].split('.')
        kezdet_year = int(kezdetstrtomb[0])
        kezdet_month = int(kezdetstrtomb[1])
        kezdet_day = int(kezdetstrtomb[2])

        vegstrtomb = sortomb[3].split('.')
        veg_year = int(vegstrtomb[0])
        veg_month = int(vegstrtomb[1])
        veg_day = int(vegstrtomb[2])

        Kuldetes.objects.create(
            az=int(sortomb[0]),
            megnevezes=sortomb[1],
            kezdet=date(kezdet_year, kezdet_month, kezdet_day),
            veg=date(veg_year, veg_month, veg_day),
        )

    return render(request, template, context)


@login_required
def kapcsolat_feltoltese_view(request):
    template = 'feltoltes_kapcsolat.html'
    context = {}
    return render(request, template, context)

@login_required
def kapcsolat_feltoltese_view_kuld(request):
    template = 'feltoltes_kuldetes_kuld.html'
    context = {}
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')

    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        az_urhajos = Urhajos.objects.get(az=int(sortomb[0])) 
        a_kuldetes = Kuldetes.objects.get(az=int(sortomb[1])) 
        a_kuldetes.resztvevoi.add(az_urhajos)

    return render(request, template, context)
