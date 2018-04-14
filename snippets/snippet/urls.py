from django.conf.urls import url
from . import views as app_views


urlpatterns = [
	url(r'^new-snippet/$', app_views.new_snippet, name='new_snippet'),
	url(r'^(?P<snippet_id>\d+)/$', app_views.snippet_detail, name='snippet_detail'),
	url(r'^edit/(?P<snippet_id>\d+)/$', app_views.edit_snippet, name='edit_snippet'),
	url(r'^delete/(?P<snippet_id>\d+)/$', app_views.delete_snippet, name='delete_snippet'),
]