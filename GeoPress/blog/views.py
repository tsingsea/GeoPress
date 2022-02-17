from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def article(request):
    return render(request, 'blog/article/index.html')