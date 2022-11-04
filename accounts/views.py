from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def first(request):
    return render(request, 'accounts/first.html')

def second(request):
    return render(request, 'accounts/second.html')

def third(request):
    return render(request, 'accounts/third.html')

def fourth(request):
    return render(request, 'accounts/fourth.html')

def complete(request):
    return render(request, 'accounts/complete.html')