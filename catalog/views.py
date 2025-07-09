from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

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


class ProductDetailView(DetailView):
    model = Product


# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "products_list.html", context)


# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)
