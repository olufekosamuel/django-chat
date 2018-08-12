from django.conf.urls import include, url
from django.urls import path
from . import views 
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', views.IndexViewSet, base_name='index')

app_name = 'chat'

#Urls for Chat App
urlpatterns = [
	url(r'^api/', include(router.urls)),
    url(r'^$', views.index, name= 'index'),
    url(r'^channel/(?P<channel_id>\d+)/$', views.index, name= 'channel'),
    url(r'^register/', views.add_user, name='register'),
    url(r'^createchannel/', views.create_channel, name='create_channel'),
    url(r'^logout/', views.logout, name='logout'),
]
