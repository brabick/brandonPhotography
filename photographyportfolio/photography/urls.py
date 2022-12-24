from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/landscape', views.landscape, name='landscape'),
    path('/contact', views.contact, name='contact'),
    path('/blog', views.PostList.as_view(), name='blog'),
    path('/blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]