from django.shortcuts import render

def index(request):

    return render(request, 'grandchildren/index.html')

def sentiment(request):

    return render(request, 'grandchildren/sentiment.html')

def setting(request):

    return render(request, 'grandchildren/setting.html')