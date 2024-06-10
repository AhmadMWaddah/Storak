from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .models import Order


# class OrderCreateView(CreateView):
#     model = Order
#     form_class = OrderCreateForm
#     success_url = reverse_lazy('Orders:OrderDetailsUrl')

#     @login_required
#     def dispatch(self, request, *args, **kwargs):
#         return super(OrderCreateView, self).dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
