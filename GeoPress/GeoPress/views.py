from django.shortcuts import render, HttpResponse, redirect
from . import urls

def home(request):
    # return redirect(
    #     'article/'
    #     # 'https://www.tsingsea.com'
    # )
    return render(request, 'GeoPress/home.html')

def login(request):
    return render(request, 'GeoPress/login.html')