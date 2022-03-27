# Django Imports
from django.contrib import admin
from django.urls import path

# Page Renders
from landing.views import landing
from login.views import login_pg
from signup.views import signup
from dashboard.views import dashboard, resources, settings, about

# APIs
from dashboard.views import get_weight, get_height, get_BMI, log_out

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('login/', login_pg, name='login'),
    path('signup', signup,  name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('resources/', resources, name="resources"),
    path('settings/', settings, name="settings"),
    path('about/', about, name="about"),
    path('api/weight', get_weight),
    path('api/height', get_height),
    path('api/BMI', get_BMI),
    path('logout', log_out),
]
