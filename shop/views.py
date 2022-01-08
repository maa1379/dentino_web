from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .forms import CategoryForm, ProductForm
from .models import Category, Product


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "shop/product_list.html"


class ProductDetail(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "shop/product_update.html"
    slug_url_kwarg = "id"
    slug_field = "id"
    success_url = reverse_lazy("shop:product_list")
    form_class = ProductForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("shop:product_list")
    template_name = "shop/product_create.html"


def ProductDeleteView(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("shop:product_list")


class CategoryListView(ListView):
    queryset = Category.objects.filter(parent__isnull=True)
    template_name = "shop/category_list.html"


class SubCategoryListView(View):

    def get(self, request, id, *args, **kwargs):
        category = Category.objects.filter(id=id)
        return render(request, "shop/subcategory_list.html", {"category": category})


class CategoryDetail(DetailView):
    model = Category
    template_name = "shop/product_detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "shop/category_update.html"
    slug_url_kwarg = "id"
    slug_field = "id"
    success_url = reverse_lazy("shop:category_list")
    form_class = CategoryForm


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("shop:category_list")
    template_name = "shop/category_create.html"


def CategoryDeleteView(request, id):
    product = get_object_or_404(Category, id=id)
    product.delete()
    return redirect("shop:category_list")
