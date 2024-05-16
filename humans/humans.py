from django.views.generic.base import TemplateView


class SignUpView(TemplateView):
    template_name = "humans/signup.html"

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context["page"] = "Sign Up"
        return context


class SignInView(TemplateView):
    template_name = "humans/signin.html"

    def get_context_data(self, **kwargs):
        context = super(SignInView, self).get_context_data(**kwargs)
        context["page"] = "Sign In"
        return context


class AccountView(TemplateView):
    template_name = "humans/account.html"

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context["page"] = "My Account"
        return context
