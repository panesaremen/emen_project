from django.contrib.auth.views import login,logout
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='song-detail'),
    url(r'^register/$', views.register,name='register'),
    url(r'^login/$', login, {'template_name': 'movie1/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'movie1/logout.html'}, name='logout'),
    url(r'^emenmovieocean/$', views.youtube_search, name='youtube_search'),
    url(r'^emenmovieocean/upload$', views.upload_handler, name='basic_upload'),


]
