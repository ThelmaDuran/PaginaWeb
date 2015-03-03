from django.conf.urls import patterns, include, url
from misDatos import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    #
)
