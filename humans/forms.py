from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm,
)
from .models import Human


class HumanSignUpForm(UserCreationForm):
    class Meta:
        model = Human
        fields = [
            "email",
            "first_name",
            "last_name",
            "user_name",
            "password1",
            "password2",
        ]

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form__input",
                "placeholder": "E-Mail ...",
                "name": "email",
                "id": "email",
            }
        ),
        label="E-Mail",
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form__input",
                "placeholder": "First Name ...",
                "name": "first-name",
                "id": "first-name",
            }
        ),
        label="First Name",
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form__input",
                "placeholder": "Last Name ...",
                "name": "last-name",
                "id": "last-name",
            }
        ),
        label="Last Name",
    )
    user_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form__input",
                "placeholder": "User Name ...",
                "name": "user-name",
                "id": "user-name",
            }
        ),
        label="User Name",
    )
    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form__input",
                "placeholder": "Password ...",
                "name": "password1",
                "id": "password1",
            }
        ),
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form__input",
                "placeholder": "Confirm Password ...",
                "name": "password2",
                "id": "password2",
            }
        ),
        label="Confirm Password",
    )


class HumanSignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(HumanSignInForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form__input",
                "placeholder": "E-Mail ...",
                "type": "email",
                "name": "email",
                "id": "email",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "class": "form__input",
                "placeholder": "Password ...",
                "type": "password",
                "name": "password",
                "id": "password",
            }
        )


class HumanPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form__input",
                "placeholder": "Old Password ...",
                "name": "old-password",
                "id": "old-password",
            }
        ),
        label="Old Password",
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form__input",
                "placeholder": "New Password ...",
                "name": "new_password1",
                "id": "new_password1",
            }
        ),
        label="New Password",
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form__input",
                "placeholder": "Confirm New Password ...",
                "name": "new_password2",
                "id": "new_password2",
            }
        ),
        label="Confirm New Password",
    )


class HumanPasswordResetForm(PasswordResetForm):
    class Meta:
        model = Human

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form__input",
                "placeholder": "E-Mail ...",
                "name": "email",
                "id": "email",
            }
        ),
        label="E-Mail",
    )


class HumanPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form__input",
                "placeholder": "New Password ...",
                "name": "password1",
                "id": "password1",
            }
        ),
        label="New Password",
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form__input",
                "placeholder": "Confirm New Password ...",
                "name": "password2",
                "id": "password2",
            }
        ),
        label="Confirm New Password",
    )
