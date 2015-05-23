from django.conf.urls import patterns, url
from .views import AddUser

urlpatterns = patterns('', 
                       url(r'add/$',
                           AddUser.as_view(),),)
