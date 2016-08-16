from django.conf.urls import url

from . import views

app_name = 'forum'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<user_id>[0-9]+)/$', views.user, name='user'),
    url(r'^login/', views.login, name='login'),


]
