from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'^$', views.sign, name='sign'),
]