from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import BagItem
from products.models import Product
from .utilities import Bag

# from orders.forms import OrderCreateForm


class BagDetailsView(ListView):
    model = BagItem
    template_name = "bags/bag_details.html"
    context_object_name = "bag_items"

    def get_context_data(self, **kwargs):
        context = super(BagDetailsView, self).get_context_data(**kwargs)
        bag = Cart(self.request)
        context["page_title"] = f"{request.user} - Bag"
        context["bag_items"] = bag.get_bag_items()
        context["total_price"] = bag.get_total_price()
        return context

    @login_required
    def dispatch(self, request, *args, **kwargs):
        return super(BagDetailsView, self).dispatch(request, *args, **kwargs)


class AddToBagView(CreateView):
    model = BagItem
    fields = []
    template_name = "bags/bag_details.html"

    def get_form_kwargs(self):
        kwargs = super(AddToBagView, self).get_form_kwargs()
        kwargs["data"] = {
            "slug": self.kwargs["slug"],
            "quantity": 1,
        }  # Set initial data
        return kwargs

    def form_valid(self, form):
        bag = Bag(self.request)
        product = Product.objects.get(slug=self.kwargs["slug"])
        bag.add(product)
        return redirect("Bags:BagDetailsUrl")

    def get_success_url(self):
        return reverse_lazy("Bags:BagDetailsUrl")


class UpdateBagItemView(UpdateView):
    model = BagItem
    fields = ["quantity"]

    def get_success_url(self):
        return reverse_lazy("Bags:BagDetailsUrl")

    def form_valid(self, form):
        form.save()
        return super(UpdateBagItemView, self).form_valid(form)


@login_required
def remove_from_bag_view(request, slug):
    bag = Bag(request)
    product = Product.objects.get(slug=slug)
    bag.remove(product)
    return redirect("Bags:BagDetailsUrl")
