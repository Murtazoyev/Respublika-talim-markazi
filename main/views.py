from django.shortcuts import render

# Create your views here.


def index(request):
    ctx = {}
    return render(request, 'main/index.html', ctx)


def about(request):
    ctx = {}
    return render(request, 'main/about.html', ctx)


def contact(request):
    ctx = {}
    return render(request, 'main/contact.html', ctx)
