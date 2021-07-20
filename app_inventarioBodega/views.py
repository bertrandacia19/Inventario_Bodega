from django.shortcuts import get_object_or_404, render,redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Bodega,Empleado

@login_required()
def index(request):
    return render(request, 'bodega/index.html')
