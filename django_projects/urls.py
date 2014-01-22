from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from pyjunkee import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_projects.views.home', name='home'),
    # url(r'^django_projects/', include('django_projects.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^post/', include('post.urls')),
     url(r'^scaffold/', include('scaffold.urls')),
     url(r'^crud/', include('crud.urls')),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
