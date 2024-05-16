from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["page"] = "Home"
        return context


class AboutView(TemplateView):
    template_name = "pages/about/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["page"] = "About Us"
        return context


class ContactView(TemplateView):
    template_name = "pages/contact/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context["page"] = "Contact Us"
        return context


class NotFoundView(TemplateView):
    template_name = "pages/not_found/404.html"

    def get_context_data(self, **kwargs):
        context = super(NotFoundView, self).get_context_data(**kwargs)
        context["page"] = "404 Not Found"
        return context
