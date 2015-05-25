from django.conf.urls import patterns, url
from .views import AddUser, AddDetails, UserDelete, ListAllUser, ListUser

urlpatterns = patterns('', 
                       url(r'add/$',
                           AddUser.as_view(),),
                       url(r'add/details/$',
                           AddDetails.as_view(),),
                       url(r'delete/$',
                           UserDelete.as_view(),),
                       url(r'list/all/$',
                           ListAllUser.as_view(),),
                       url(r'(?P<user_id>[0-9]+)/list/$',
                           ListUser.as_view(),),)

