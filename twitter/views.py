from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .forms import CustomAuthenticationForm, CustomCreationForm
from .models import Profile

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'landing/login.html'
    redirect_authenticated_user = True
    next_page = 'twitter:timeline'
    form_class = CustomAuthenticationForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pagename'] = "login"
        return context


class RegisterView(CreateView):
    form_class = CustomCreationForm
    template_name = "landing/register.html"
    success_url = "/"


def logout_view(request):
    logout(request)
    return redirect("twitter:login")


@login_required(login_url="/login")
def timeline(request):
    return render(request, "twitter/base_app.html", {})


@login_required(login_url="/login")
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "twitter/profiles.html", {
        "profiles": profiles,
    })


@login_required(login_url="/login")
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    
    return render(request, "twitter/profile.html", {
        "profile": user_profile
    })

@login_required(login_url="/login")
def other_profiles(request, pk):
    user_profile = Profile.objects.get(id=pk)
    
    return render(request, "twitter/profile.html", {
        "profile": user_profile
    })
