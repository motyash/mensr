from django.shortcuts import render
from django.http import HttpResponse
from .models import Clothing

def index(request):
    return render(request, 'index.html')



def clothing(request):
    clothing_list = Clothing.objects.all()
    return render(request, 'clothing.html', {'clothing_list': clothing_list})



def about(request):
    return render(request, 'О-нас.html')