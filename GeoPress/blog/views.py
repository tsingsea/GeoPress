from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def article(request):
    return HttpResponse('这是文章页')