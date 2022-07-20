from django.contrib import admin
from django.urls import path
from . import views
from .views import  BlogDetailView
#BlogListView

urlpatterns = [
    # path("",views.blog_index , name="blog_index"),
    path('', views.blog_index, name='blog'),
    #path("",views.blog_detail , name="blog_detail"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
