from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def dbconnect(request):

    return render(request, 'dbconnect.html')

def chat(request):

    return render(request, 'chat.html')
