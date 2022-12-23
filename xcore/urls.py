from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from yasg import urlpatterns as doc_urls
from router import DefaultRouter
from api.urls import router as api_routers

router = DefaultRouter()
router.extend(api_routers)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1', include(router.urls)),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
