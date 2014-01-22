from django.conf.urls import patterns, url

urlpatterns = patterns('scaffold.views',
     # scaffold app
     url(r'^content/$', 'content', ), 
     url(r'^login/$', 'login_view',), 
     url(r'^logout/$', 'logout_view',), 
)
