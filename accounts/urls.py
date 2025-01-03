from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, PasswordResetView, PasswordResetConfirmView, PasswordChangeView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls + [
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
]