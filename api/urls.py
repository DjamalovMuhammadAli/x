from xcore.router import DefaultRouter
from api.user.urls import router as user_router
# from api.content.urls import router as content_couter

router = DefaultRouter()

router.extend(user_router)
