from django.urls import path

from .views import RegisterWithPhoneNumber, UpdateUserView, VerifyUserRegister

app_name = "account_api"
urlpatterns = [
    path("", UpdateUserView.as_view(), name="update"),
    path("verify/", VerifyUserRegister.as_view(), name="verify"),
    path("register/", RegisterWithPhoneNumber.as_view(), name="register"),
]
