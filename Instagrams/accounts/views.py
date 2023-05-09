from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView,
    logout_then_login,
    PasswordChangeView as AuthenticationView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render


from .forms import SignupForm, ProfileForm, PasswordChangeForm



login = LoginView.as_view(template_name="accounts/login_form.html")


def logout(request):
    messages.success(request, "Logout Success")
    return logout_then_login(request)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Signup Success")
            return redirect("/")
    else:
        form = SignupForm()
    return render(
        request,
        "accounts/signup_form.html",
        {
            "form": form,
        },
    )


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필을 수정/저장 했습니다.")
            return redirect("profile_edit")
    else:
        form = ProfileForm(instance=request.user)
    return render(
        request,
        "accounts/profile_edit_form.html",
        {
            "form": form,
        },
    )


class PasswordChangeView(LoginRequiredMixin, AuthenticationView):
    success_url = reverse_lazy("password_change")
    template_name = "accounts/password_change_form.html"
    form_class = PasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, "암호가 성공적으로 변경 되었습니다. ")
        return super().form_valid(form)

password_change = PasswordChangeView.as_view()
