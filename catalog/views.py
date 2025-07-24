from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import get_products_from_cache, get_products_by_category


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

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm("catalog.can_unpublish_product"):
            return ProductForm
        raise PermissionDenied("У вас нет прав на редактирование этого продукта.")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/catalog_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user != product.owner and not request.user.has_perm(
            "catalog.can_delete_product"
        ):
            raise PermissionDenied("У вас нет прав на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)


# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "products_list.html", context)


# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)


class ListProductsCategory(DetailView):
    model = Category
    template_name = "catalog/products_by_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs.get("category_id"))
        context["category"] = category
        return context

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return get_products_by_category(category_id)
