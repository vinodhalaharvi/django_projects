from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from pyjunkee import views
from scaffold import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_projects.views.home', name='home'),
    # url(r'^django_projects/', include('django_projects.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     #url(r'^index/$', views.index, name='index'), 
     # crud app
     #url(r'^content/$', views.content, name='content'), 
     #url(r'^books/update/(?P<id>\d{1,4})/$', views.update, name='update'), 
     #url(r'^books/delete/(?P<id>\d{1,4})/$', views.delete, name='delete'), 
     #url(r'^books/detail/(?P<id>\d{1,4})/$', views.detail, name='detail'), 
     #url(r'^books/list/(?P<id>\d{1,4})/$', views.list, name='list'), 
     #url(r'^books/new/$', views.new, name='new'), 
     #url(r'^books/list/$', views.list, name='list'), 
     #url(r'^login/$', views.login_view, name='login_view'), 
     #url(r'^logout/$', views.logout_view, name='logout_view'), 

     # scaffold app
     url(r'^content/$', views.content, name='content'), 
     url(r'^login/$', views.login_view, name='login_view'), 
     url(r'^logout/$', views.logout_view, name='logout_view'), 

)
