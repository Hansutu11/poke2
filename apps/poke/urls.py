from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^dashboard/(?P<user_id>\d+)$', views.increment),
]
