from django.urls import path

from .views import (CategoryCreateView, CategoryDeleteView, CategoryDetail,
                    CategoryListView, CategoryUpdateView, ProductCreateView,
                    ProductDeleteView, ProductDetail, ProductListView,
                    ProductUpdateView, SubCategoryListView)

app_name = "shop"

urlpatterns = [
    path("product/", ProductListView.as_view(), name="product_list"),
    path("product/<int:id>/", ProductDetail.as_view(), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/update/<int:id>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path("product/delete/<int:id>/", ProductDeleteView, name="product_delete"),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path(
        "category/update/<int:id>/",
        CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "category/delete/<int:id>/",
        CategoryDeleteView,
        name="category_delete",
    ),
    path("category/detail/<int:id>/", CategoryDetail.as_view(), name="category_detail"),
    path("category/sub/<int:id>/", SubCategoryListView.as_view(), name="category_sub"),
]
