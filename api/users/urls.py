from django.conf.urls import patterns, url
from .views import AddUser, AddDetails, UserDelete

urlpatterns = patterns('', 
                       url(r'add/$',
                           AddUser.as_view(),),
                       url(r'add/details/$',
                           AddDetails.as_view(),),
                       url(r'delete/$',
                           UserDelete.as_view(),),)

