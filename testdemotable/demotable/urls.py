from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all/", views.all, name="all"),
    path("filterid/<int:id>", views.filterid, name="filterid"),
]