from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'loading/index.html')

def info(request):
    return render(request, 'loading/info.html')