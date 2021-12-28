from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import urls
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import paymentno, paymentok

urlpatterns = [
    path("", include("shop.urls", namespace="shop")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/", include("rest_framework.urls"), name="reset"),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("course/", include("commoncourse.urls", namespace="common_course")),
    path("api/", include("api.urls", namespace="api")),
    path("admin/", admin.site.urls),
    path("", include("partial.urls", namespace="partial")),
    path("location/", include("location.urls", namespace="location")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("clinic/", include("clinic.urls", namespace="clinic")),
    path("", include("doctor.urls", namespace="doctor")),
    path("account/", include("account.urls", namespace="account")),
    path("", include("reservation.urls", namespace="reserve")),
    path("", include("blog.urls", namespace="blog")),
    path("api/", include("api.urls", namespace="api")),
    path("", include("config.urls", namespace="config")),
    path("paymentok/", paymentok.as_view(), name="payment_ok"),
    path("paymentno/", paymentno.as_view(), name="payment_no"),
]
if settings.DEBUG:
    # ADD ROOT MEDIA FILES
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
