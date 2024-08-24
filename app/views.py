from django.shortcuts import render

# Create your views here.

def ammu(request):
    return render(request,'ammu.html')

def siri(request):
    return render(request,'siri.html')

def sai(request):
    return render(request,'sai.html')

def table(request):
    return render(request,'table.html')

def heading(request):
    return render(request,'heading.html')