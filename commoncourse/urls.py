from django.urls import path

from .views import (CommonCourseCreate, CommonCourseDelete, CommonCourseDetail,
                    CommonCourseList, CommonCourseUpdate)

app_name = "commmon_course"
urlpatterns = [
    path("", CommonCourseList.as_view(), name="list"),
    path("create/", CommonCourseCreate.as_view(), name="create"),
    path("update/<int:pk>/", CommonCourseUpdate.as_view(), name="update"),
    path("<int:id>/", CommonCourseDetail, name="detail"),
    path("delete/<int:pk>/", CommonCourseDelete, name="delete"),
]
