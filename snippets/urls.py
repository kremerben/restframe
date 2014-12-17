from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


# API endpoints
urlpatterns = [
    url(r'^', include(router.urls)),
    # Login and logout views for the browsable API
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

]
