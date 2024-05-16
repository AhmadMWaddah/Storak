from django.views.generic.base import TemplateView


class AllProductsView(TemplateView):
    template_name = "products/shop.html"

    def get_context_data(self, **kwargs):
        context = super(AllProductsView, self).get_context_data(**kwargs)
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
