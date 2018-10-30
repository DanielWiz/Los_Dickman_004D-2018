from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$',views.inicio),
    url(r'^login/$', login , {'template_name': 'usuarios/login.html'}),
    url(r'^logout/$', logout , {'template_name': 'usuarios/logout.html'}),
]