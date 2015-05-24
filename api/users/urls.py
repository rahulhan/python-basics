from django.conf.urls import patterns, url
from .views import AddUser, AddDetails

urlpatterns = patterns('', 
                       url(r'add/$',
                           AddUser.as_view(),),
                       url(r'add/details/$',
                           AddDetails.as_view(),),)

