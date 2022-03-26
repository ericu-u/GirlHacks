from django.contrib import admin
from django.urls import path

from landing.views import landing
from login.views import login
from signup.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('login', login, name='login'),
    path('signup', signup,  name='signup'),
]
