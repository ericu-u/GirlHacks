from django.contrib import admin
from django.urls import path

from landing.views import landing
from login.views import login_pg
from signup.views import signup
from dashboard.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('login', login_pg, name='login'),
    path('signup', signup,  name='signup'),
    path('dashboard', dashboard, name='dashboard'),
]
