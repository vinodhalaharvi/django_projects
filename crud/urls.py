from django.conf.urls import patterns, url

urlpatterns = patterns('crud.views',
     # crud app
     url(r'^content/$', 'content'), 
     url(r'^books/update/(?P<id>\d{1,4})/$', 'update'), 
     url(r'^books/delete/(?P<id>\d{1,4})/$', 'delete'), 
     url(r'^books/detail/(?P<id>\d{1,4})/$', 'detail'), 
     url(r'^books/list/(?P<id>\d{1,4})/$', 'list'), 
     url(r'^books/new/$', 'new'), 
     url(r'^books/list/$', 'list'), 
     url(r'^login/$', 'login_view'), 
     url(r'^logout/$', 'logout_view'), 
)
