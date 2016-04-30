from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'thanks', views.thanks, name='thanks'),
    url(r'^size/', views.size, name='size'),
    url(r'size', views.size, name='size'),
    url(r'^$', views.sign, name='sign'),
    url(r'', views.sign, name='sign'),
]
