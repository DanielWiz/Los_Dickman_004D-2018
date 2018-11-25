from django.conf.urls import url,include
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.inicio),
    path('', include('social_django.urls', namespace='social')),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="usuarios/login.html"),name='login'),
    url(r'^registro/$', views.RegistroDatos,name='registro'),
    url(r'^adopcion/$', views.adopcion,),
    url(r'^logout/$', auth_views.LogoutView, {'next_page':'/'}, name='logout'),
    path('perro/<int:pk>/', views.detalle_perro, name='detalle_perro'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)