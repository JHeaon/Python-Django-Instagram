from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm
from .models import User
from .models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("Email already")

        return email

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["website_url", "bio", "phone_number", "gender"]


class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password2(self) -> str:
        old_password = self.cleaned_data.get('old_password')
        new_password2 = super().clean_new_password2()
        if old_password == new_password2:
            raise forms.ValidationError("새로운 암호는 기존 암호와 다르게 입력하여야 합니다.")
        return new_password2