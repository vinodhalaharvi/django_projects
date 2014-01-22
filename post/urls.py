from django.conf.urls import patterns, url

urlpatterns = patterns('post.views',
    url(r'^$', 'index'),
    url(r'^(?P<post_id>\d+)/$', 'post'),
    url(r'^post/$', 'index'),
    url(r'^login/$', 'login_view',),
    url(r'^logout/$', 'logout_view',),
)
