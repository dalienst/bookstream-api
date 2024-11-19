from django.urls import path

from accounts.views import (
    UserCreateView,
    UserDetailView,
    UserListView,
    SignInView,
    LogoutView,
)

urlpatterns = [
    path("token/", SignInView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", UserCreateView.as_view(), name="register"),
    path("<str:id>/", UserDetailView.as_view(), name="user_detail"),
    path("", UserListView.as_view(), name="user_list"),
]
