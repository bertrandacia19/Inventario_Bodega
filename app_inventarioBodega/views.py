from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bodega/index.html')

def base(request):
    return render(request, "global_templates/base.html")