from django.conf.urls import patterns, include, url
from django.contrib import admin
from snippets import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restframe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
)
