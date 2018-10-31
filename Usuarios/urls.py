from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.inicio),
    url(r'^login/$', views.login ),
    url(r'^logout/$', views.logout),
    url(r'^registro/$', views.registro,name='registro'),
    url(r'^adopcion/$', views.adopcion,),
]