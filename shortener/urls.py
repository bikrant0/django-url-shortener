from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('shorten/', views.create_short_url),
    path('<str:short_alias>/', views.redirect_url),
]