from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    print(request.POST['tsv_szoveg'])
    return render(request, template, context)

