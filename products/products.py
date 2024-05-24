from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Product


class AllProductsView(TemplateView):
    model = Product
    context_object_name = "products"
    template_name = "products/shop.html"

    def get_queryset(self):
        queryset = Product.objects.filter(in_stock=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AllProductsView, self).get_context_data(**kwargs)
        context["products"] = self.get_queryset()
        context["products_count"] = self.get_queryset().count()
        context["page"] = "All Products"
        return context


class ProductDetailsView(TemplateView):
    template_name = "products/details.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailsView, self).get_context_data(**kwargs)
        context["page"] = "Product Details"
        return context


class CompareProductsView(TemplateView):
    template_name = "products/compare.html"

    def get_context_data(self, **kwargs):
        context = super(CompareProductsView, self).get_context_data(**kwargs)
        context["page"] = "Compare Products"
        return context
