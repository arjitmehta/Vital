from django.urls import path,re_path
from . import views
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
    # path('<str:aasan>/', views.index, name='aasan'),
]
websocket_urlpatterns = [
    re_path(r'ws/video-feed/(?P<aasan>[^/]+)/$', views.VideoProcessorConsumer.as_asgi()),
]

# Add the following lines to include websocket_urlpatterns
# application = ProtocolTypeRouter({
#     "http": URLRouter(urlpatterns),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(websocket_urlpatterns)
#     ),
# })