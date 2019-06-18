from django.conf.urls import url
from django.contrib import admin
# from posts.views import post_create

from posts.views import *
# from posts.views import post_update
# from posts.views import post_detail
# from posts.views import post_list


urlpatterns = [

    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name="delete"),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
    # url(r'^list/$', post_list, name="list"),
    # url(r'^$', post_list, name="list"),
    url(r'^$', List.as_view(), name="list")
]
