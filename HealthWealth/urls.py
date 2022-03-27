from django.contrib import admin
from django.urls import path

from landing.views import landing
from login.views import login_pg
from signup.views import signup
from dashboard.views import dashboard, get_weight, resources, settings, about, log_out

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
    path('logout', log_out),
]
