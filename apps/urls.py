from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("mainpage", views.main_page, name="mainpage"),
    path('home', views.home, name="home"),
    path('reset', views.passreset, name="reset"),
    path('logout', views.log_out, name="logout"),
    path('upload', views.upload, name='upload')
]