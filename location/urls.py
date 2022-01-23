from django.urls import path

from .views import (
    CityCreateView,
    CityDeleteView,
    CityListView,
    CityUpdateView,
    ProvinceCreate,
    ProvinceDelete,
    ProvinceDetail,
    ProvinceListView,
    ProvinceUpdate,
    ZoneCreate,
    ZoneDeleteView,
    ZoneListView,
    ZoneUpdate,
)

app_name = "Location"
urlpatterns = [
    path("", ProvinceListView.as_view(), name="province"),
    path("city_list/", CityListView.as_view(), name="city_list"),
    path("city_create/", CityCreateView.as_view(), name="city_create"),
    path("city_update/<int:id>/", CityUpdateView.as_view(), name="city_update"),
    path("city_delete/<int:id>/", CityDeleteView, name="city_delete"),
    path("zone_create/", ZoneCreate.as_view(), name="zone_create"),
    path("zone_update/<int:id>/", ZoneUpdate.as_view(), name="zone_update"),
    path("zone_delete/<int:id>/", ZoneDeleteView, name="zone_delete"),
    path("zone_list/", ZoneListView.as_view(), name="zone_list"),
    path("", ProvinceListView.as_view(), name="province"),
    path("province/create/", ProvinceCreate.as_view(), name="province_create"),
    path("province/update/<int:id>/", ProvinceUpdate.as_view(), name="province_update"),
    path("province/delete/<int:id>/", ProvinceDelete, name="province_delete"),
    path("province/detail/<int:pk>/", ProvinceDetail.as_view(), name="province_detail"),
    # path("city/<int:province>/", CityListView.as_view(), name="city"),
    path("zone/<int:city>/", ZoneListView.as_view(), name="Zone"),
    # path("create/", LocationCreateView.as_view(), name="Create"),
    # path("update/<int:id>/", LocationUpdateView.as_view(), name="update"),
    # path("delete/<int:id>/", LocationDeleteView, name="delete"),
    # path("<str:name>/", City_Of_Province_ListView.as_view(), name="Detail"),
]
