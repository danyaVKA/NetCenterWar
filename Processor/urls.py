from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('polite', views.polite, name='polite'),
    path('economic', views.economic, name='economic'),
    path('stocks', views.stocks, name='stocks'),
    path('business', views.business, name='business'),
    path('datacollection', views.datacollection, name='datacollection'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
]
