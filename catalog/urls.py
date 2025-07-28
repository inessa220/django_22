from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    HomeView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, ListProductsCategory,
)


app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path(
        "catalog/<int:pk>/",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("products/category/<int:category_id>/", ListProductsCategory.as_view(), name="products_by_category"),
]
