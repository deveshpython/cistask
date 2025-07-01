from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet, RegisterViewSet

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls

