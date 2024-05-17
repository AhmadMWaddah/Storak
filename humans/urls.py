from django.urls import path
from .humans import (
    HumanSignUpView,
    HumanSignInView,
    HumanSignOutView,
    HumanDetailsView,
    HumanPasswordChangeView,
    HumanPasswordChangeDoneView,
    HumanPasswordResetView,
    HumanPasswordResetDoneView,
    HumanPasswordResetConfirmView,
    HumanPasswordResetCompleteView,
)


app_name = "Humans"


urlpatterns = [
    path("sign-up", HumanSignUpView.as_view(), name="HumanSignUpUrl"),
    path("sign-in", HumanSignInView.as_view(), name="HumanSignInUrl"),
    path("sign-out", HumanSignOutView.as_view(), name="HumanSignOutUrl"),
    path("my-account/<slug:slug>", HumanDetailsView.as_view(), name="HumanDetailsUrl"),
    path(
        "password-change",
        HumanPasswordChangeView.as_view(),
        name="HumanPasswordChangeUrl",
    ),
    path(
        "password-change/done",
        HumanPasswordChangeDoneView.as_view(),
        name="HumanPasswordChangeDoneUrl",
    ),
    path(
        "password-reset", HumanPasswordResetView.as_view(), name="HumanPasswordResetUrl"
    ),
    path(
        "password-reset/done",
        HumanPasswordResetDoneView.as_view(),
        name="HumanPasswordResetDoneUrl",
    ),
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        HumanPasswordResetConfirmView.as_view(),
        name="HumanPasswordResetConfirmUrl",
    ),
    path(
        "password-reset/complete",
        HumanPasswordResetCompleteView.as_view(),
        name="HumanPasswordResetCompleteUrl",
    ),
]
