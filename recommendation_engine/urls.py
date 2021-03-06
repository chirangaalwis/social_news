from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.frontpage, name='frontpage'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
