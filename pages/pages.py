from django.views.generic.base import TemplateView
from products.models import Category, Product


class HomeView(TemplateView):
    template_name = "pages/home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["categories"] = Category.objects.only()
        context["products"] = Product.objects.only()
        context["trendings"] = Product.objects.only().filter(badge="Trending")[:3]
        context["featureds"] = Product.objects.only().filter(badge="Featured")[:3]
        context["best_sellers"] = Product.objects.only().filter(badge="Best Seller")[:3]
        context["new_arrivals"] = Product.objects.only().filter(badge="New Arrival")[:3]

        context["trends_products"] = Product.objects.only().filter(badge="Trending")[:4]
        context["feat_products"] = Product.objects.only().filter(badge="Trending")[:4]
        context["best_products"] = Product.objects.only().filter(badge="Trending")[:4]

        context["page_title"] = "Home"
        return context


class AboutView(TemplateView):
    template_name = "pages/about/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["page_title"] = "About Us"
        return context


class ContactView(TemplateView):
    template_name = "pages/contact/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context["page_title"] = "Contact Us"
        return context


class NotFoundView(TemplateView):
    template_name = "pages/not_found/404.html"

    def get_context_data(self, **kwargs):
        context = super(NotFoundView, self).get_context_data(**kwargs)
        context["page_title"] = "404 Not Found"
        return context
