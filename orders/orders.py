from django.views.generic.base import TemplateView


class CheckOutView(TemplateView):
    template_name = "bags/checkout.html"

    def get_context_data(self, **kwargs):
        context = super(CheckOutView, self).get_context_data(**kwargs)
        context["page"] = "Checkout"
        return context
