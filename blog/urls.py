from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	url(r'^ps/$', views.PostListView.as_view(), name='posts'),
	url(r'^p/(?P<pk>[-\w]+)$', views.PostDetailView.as_view(), name='post-detail'),
	url(r'^p/add/$', views.PostCreate.as_view(), name='post-create'),
	url(r'^p/(?P<pk>[-\w]+)/upd/$', views.PostUpdate.as_view(), name='post-update'),

]
