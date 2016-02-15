from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^404', views.error404, name='404'),
    url(r'^$', views.home, name='home'),
]