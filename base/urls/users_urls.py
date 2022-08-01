from django.urls import include, path
from base.views import users_views as views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from base.views.users_views import MyTokenObtainPairView

urlpatterns = [
    # path('', views.get_routes, name='routes'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.register_user, name='register_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.edit_profile, name='edit_refresh'),
    path('', views.get_users, name='get_users'),
    path('<str:pk>/edit/', views.edit_user, name='edit_user'),
    path('<str:pk>/delete/', views.delete_user, name='delete_user'),
]
