from django.urls import path

from .views import BlogCreate, BlogDetail, BlogList

app_name = "blog"

urlpatterns = [
    path("blog/", BlogList.as_view(), name="list"),
    path("blog/create/", BlogCreate.as_view(), name="create"),
    path("blog/<slug>/", BlogDetail.as_view(), name="detail"),
]
