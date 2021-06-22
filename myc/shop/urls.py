from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name='shop'),
    path("search", views.search, name='search'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("tracker", views.tracker, name='tracker'),
    path("proview/<int:myid>", views.proview, name='proview'),
    path("checkout", views.checkout, name='checkout')
]