from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.inicio),
    url(r'^login/$', views.login , {'template_name': 'usuarios/login.html'}),
    url(r'^logout/$', views.logout , {'template_name': 'usuarios/logout.html'}),
    url(r'^registro/$', views.registro,name='registro'),
]