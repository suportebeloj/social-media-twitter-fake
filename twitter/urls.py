from django.urls import path
from .views import *

app_name = "twitter"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', logout_view, name="logout"),
    path('', timeline, name="timeline"),
    path('profiles/', profile_list, name="profiles"),
    path('profile/', profile, name="profile"),
    path('profile/<int:pk>', other_profiles, name="other_profiles")
]
