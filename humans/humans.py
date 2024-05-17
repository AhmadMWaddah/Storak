# Django Imports.
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import (
    LogoutView,
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from .forms import (
    HumanSignUpForm,
    HumanSignInForm,
    HumanPasswordResetForm,
    HumanPasswordResetConfirmForm,
    HumanPasswordChangeForm,
)
from django.urls import reverse_lazy
from .models import Human


class HumanSignUpView(CreateView):
    template_name = "humans/signup.html"
    form_class = HumanSignUpForm

    def get_success_url(self):
        return reverse_lazy("Humans:HumanSignInUrl")

    def get_context_data(self, **kwargs):
        context = super(HumanSignUpView, self).get_context_data(**kwargs)
        context["page"] = "Sign Up"
        return context


class HumanSignInView(LoginView):
    template_name = "humans/signin.html"
    form_class = HumanSignInForm

    def get_success_url(self):
        return reverse_lazy("Pages:HomeUrl")

    def get_context_data(self, **kwargs):
        context = super(HumanSignInView, self).get_context_data(**kwargs)
        context["page"] = "Sign In"
        return context


class HumanSignOutView(LogoutView):
    next_page = reverse_lazy("Humans:HumanSignInUrl")


class HumanDetailsView(DetailView):
    model = Human
    template_name = "humans/account.html"

    def get_context_data(self, **kwargs):
        context = super(HumanDetailsView, self).get_context_data(**kwargs)
        context["page"] = f"{self.object.user_name} - Profile"
        return context


class HumanPasswordChangeView(PasswordChangeView):
    template_name = "humans/password_change.html"
    form_class = HumanPasswordChangeForm
    success_url = reverse_lazy("Humans:HumanPasswordChangeDoneUrl")

    def get_context_data(self, **kwargs):
        context = super(HumanPasswordChangeView, self).get_context_data(**kwargs)
        context["page"] = "Change Password"
        return context


class HumanPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "humans/password_change_done.html"

    def get_context_data(self, **kwargs):
        context = super(HumanPasswordChangeDoneView, self).get_context_data(**kwargs)
        context["page"] = "Change Password Done"
        return context


class HumanPasswordResetView(PasswordResetView):
    template_name = "humans/password_reset.html"
    email_template_name = "humans/password_reset_email.html"
    form_class = HumanPasswordResetForm
    success_url = reverse_lazy("Humans:HumanPasswordResetDoneUrl")

    def get_context_data(self, **kwargs):
        context = super(HumanPasswordResetView, self).get_context_data(**kwargs)
        context["page"] = "Reset Password"
        return context


class HumanPasswordResetDoneView(PasswordResetDoneView):
    template_name = "humans/password_reset_done.html"

    def get_context_data(self, **kwargs):
        context = super(HumanPasswordResetDoneView, self).get_context_data(**kwargs)
        context["page"] = "Reset Password Done"
        return context


class HumanPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "humans/password_reset_confirm.html"
    form_class = HumanPasswordResetConfirmForm
    success_url = reverse_lazy("Humans:HumanPasswordResetCompleteUrl")

    def get_context_data(self, **kwargs):
        context = super(HumanPasswordResetConfirmView, self).get_context_data(**kwargs)
        context["uidb64"] = self.kwargs.get("uidb64")
        context["token"] = self.kwargs.get("token")
        context["page"] = "New Password Confirm"
        return context


class HumanPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "humans/password_reset_complete.html"

    def get_context_data(self, **kwargs):
        context = super(HumanPasswordResetCompleteView, self).get_context_data(**kwargs)
        context["page"] = "Reset Password Complete"
        return context
