from django.urls import path
from . import views
# import routers
from rest_framework import routers, serializers, viewsets


urlpatterns = [
	path('', views.getRoutes, name="routes"),	
	path('notes/', views.getNotes, name="notes"),	
]


"""
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'userslist', views.MessageListView)
router.register(r'userscreate', views.MessageCreateView)
 

urlpatterns = [
	path('', include(router.urls)),
	#path('messages/', views.MessageListView.as_view(), name='message-list'),
	#path('messages/create/', views.MessageCreateView.as_view(), name='message-create'),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
"""