from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.post_list, name='home'),

url(r'^$', views.post_list, name='post_list'),
url(r'^$', views.document_list, name='document_list'),

    url(r'^list/$', views.document_list, name='document_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new2/$', views.post_new2, name='post_new2'),
]
