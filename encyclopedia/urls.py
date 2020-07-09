from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<Title>", views.entry, name="entry"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("entry/edit/<title>", views.edit, name="edit")
]
