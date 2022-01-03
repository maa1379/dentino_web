from django.urls import path

from .views import SignUpUserView, UserListView

app_name = "account"
urlpatterns = [
    path("user_list/", UserListView.as_view(), name="user_list"),
    path("user_create/", SignUpUserView, name="signup"),
]
