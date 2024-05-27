from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from products.models import Product


class BagView(TemplateView):
    template_name = "bags/bag_details.html"

    def get_context_data(self, **kwargs):
        context = super(BagView, self).get_context_data(**kwargs)
        context["page_title"] = "Shopping Bag"
        return context
