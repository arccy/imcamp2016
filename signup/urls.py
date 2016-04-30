from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'thanks', views.thanks, name='thanks'),
    url(r'^size/', views.thanks, name='sizes'),
    url(r'size', views.thanks, name='sizes'),
    url(r'^$', views.sign, name='sign'),
    url(r'', views.sign, name='sign'),
]
