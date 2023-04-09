from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import AccountLoginView

app_name = "account"

urlpatterns = [
    path("login/", AccountLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]