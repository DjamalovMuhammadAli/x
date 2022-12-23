from rest_framework import routers
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.user.views import UserViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls
