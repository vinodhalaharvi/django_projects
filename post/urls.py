from django.conf.urls import patterns, url

urlpatterns = patterns('post.views',
    url(r'^$', 'index'),
    url(r'^(?P<post_id>\d+)/$', 'post'),
    url(r'^post/$', 'index'),
)
