from django.shortcuts import render
from django.urls import path
from boards import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("board/", views.show_board),
    path("board/all", views.all - board),
]

# Create your views here.
