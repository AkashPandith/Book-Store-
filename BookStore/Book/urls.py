from django.contrib import admin
from django.urls import path
from Book import views

urlpatterns = [
    #path("",views.view1, name = "view1"),
    path("home", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("services", views.services, name = "services"),
    path("contact", views.contact, name = "contact"),
    path("store", views.store, name = "store"),
    path("rent", views.rent, name = "rent"),
    path("login", views.loginuser, name = "login"),
]
