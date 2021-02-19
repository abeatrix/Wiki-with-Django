from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>",views.entry, name="entry"),
    path("wiki/create", views.create, name="create"),
    path("wiki/edit", views.edit, name="edit"),
    path("wiki/random", views.random, name="random"),
]
