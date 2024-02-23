from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Urhajos

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
            nev=sortomb[1],
            orszag=sortomb[2],
            nem=sortomb[3],
            szulev=int(sortomb[4]),
            urido=sortomb[5],
        )

    return render(request, template, context)

