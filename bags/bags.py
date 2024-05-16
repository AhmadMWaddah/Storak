from django.views.generic.base import TemplateView


class BagView(TemplateView):
    template_name = "bags/bag_details.html"

    def get_context_data(self, **kwargs):
        context = super(BagView, self).get_context_data(**kwargs)
        context["page"] = "Shopping Bag"
        return context


class WishListView(TemplateView):
    template_name = "bags/wishlist.html"

    def get_context_data(self, **kwargs):
        context = super(WishListView, self).get_context_data(**kwargs)
        context["page"] = "Wishlist"
        return context


class CheckOutView(TemplateView):
    template_name = "bags/checkout.html"

    def get_context_data(self, **kwargs):
        context = super(CheckOutView, self).get_context_data(**kwargs)
        context["page"] = "Checkout"
        return context
