from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from .models import Category, Product


class AllProductsView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "products/shop.html"
    paginate_by = 8

    def get_queryset(self):
        queryset = Product.objects.filter(in_stock=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AllProductsView, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        page_number = self.request.GET.get("page")
        paginator = Paginator(queryset, self.paginate_by)
        if page_number is None:
            page_obj = paginator.page(1)
        else:
            page_obj = paginator.get_page(page_number)
        context["products"] = page_obj.object_list
        context["is_paginated"] = page_obj.has_other_pages()
        context["page_obj"] = page_obj
        context["paginate_by"] = self.paginate_by
        context["products_count"] = self.get_queryset().count()
        context["page_title"] = "All Products"
        return context


class ProductDetailsView(TemplateView):
    template_name = "products/details.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailsView, self).get_context_data(**kwargs)
        context["page_title"] = "Product Details"
        return context
