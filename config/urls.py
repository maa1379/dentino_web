from django.urls import path

from .views import (
    AboutUS_View,
    AddSliderView,
    HomeView,
    PanelLoginView,
    PanelLogoutView,
    PanelView,
    SiteConfigView,
    SliderDelete,
    SliderListView,
    SliderUpdate,
)

app_name = "config"
urlpatterns = [
    path("", HomeView.as_view(), name="Home"),
    path("panel/", PanelView.as_view(), name="Panel"),
    path("login/", PanelLoginView.as_view(), name="login"),
    path("logout/", PanelLogoutView.as_view(), name="logout"),
    path("slider/", SliderListView.as_view(), name="slider_list"),
    path("add_slider/", AddSliderView.as_view(), name="slider_add"),
    path("about_us/", AboutUS_View.as_view(), name="about_us"),
    path("site_config/", SiteConfigView.as_view(), name="site_config"),
    path("slider_update/<int:id>/", SliderUpdate.as_view(), name="slider_update"),
    path("slider_delete/<int:id>/", SliderDelete.as_view(), name="slider_delete"),
]
