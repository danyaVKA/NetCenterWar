from django.shortcuts import render
from django.http import HttpResponse


def map(request):
    data = {'title': 'Map world'}
    return render(request, "Processor/map.html", data)

def polite(request):
    return render(request,"Processor/polite.html")

def economic(request):
    return render(request, "Processor/economic.html")

def stocks(request):
    return render(request, "Processor/stocks.html")

def business(request):
    return render(request, "Processor/business.html")

def datacollection(request):
    return render(request, "Processor/datacollection.html")

def about(request):
    return render(request, "Processor/about.html")

def news(request):
    return render(request,"Processor/news.html")