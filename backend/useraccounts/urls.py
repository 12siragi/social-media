from django.urls import path
from .views import (
    UserInfoView,
    UserRegistrationView,
    LoginView,
    UserProfileView,
    UserProfileUpdateView,
    LogoutView,
    CookieTokenRefreshView,
)

urlpatterns = [
    #user-info
    path("user-info/", UserInfoView.as_view(), name="user-info"),
    # User registration endpoint
    path('register/', UserRegistrationView.as_view(), name='register'),

    # User login endpoint
    path('login/', LoginView.as_view(), name='login'),

    # User profile retrieval
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    # User profile update endpoint
    path('profile/update/', UserProfileUpdateView.as_view(), name='user-profile-update'),

    # User logout endpoint
    path('logout/', LogoutView.as_view(), name='logout'),

    # Token refresh endpoint
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token-refresh'),
]
