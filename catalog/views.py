from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm
from catalog.models import Product


class HomeView(TemplateView):
    template_name = "catalog/home.html"


# def home(request):
#     return render(request, "home.html")


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


# def contacts(request):
#     return render(request, "contacts.html")


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(CreateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/catalog_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "products_list.html", context)


# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)
