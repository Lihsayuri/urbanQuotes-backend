from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/quotes', views.api_quotes),
    path('api/minhasQuotes', views.api_minhasQuotes)
]