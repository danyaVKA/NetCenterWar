from django.shortcuts import render
from .models import Articales

def news(request):
    news = Articales.objects.order_by()
    data = {'news': news}
    return render(request, 'News/news.html', data)
# Create your views here.
