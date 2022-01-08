from django.urls import path

from .views import SignUpUserView, UserListView, delete_user, UserUpdateView

app_name = "account"
urlpatterns = [
    path("user_list/", UserListView.as_view(), name="user_list"),
    path("user_create/", SignUpUserView, name="signup"),
    path("user_delete/<int:id>/", delete_user, name="user_delete"),
    path("user_update/<int:id>/", UserUpdateView, name="user_update"),
]
