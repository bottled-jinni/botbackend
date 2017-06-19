from django.conf.urls import url, include
from nodemanager import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=False)
router.register(r'nodemanager', views.NodeItemViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]