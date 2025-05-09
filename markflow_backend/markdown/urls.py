from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, CustomLoginView

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='documents')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/users/<int:id>/login/', CustomLoginView.as_view(), name='custom-login'),
]
