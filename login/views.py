from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

from .forms import log_in

# Create your views here.
def login_pg(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("heree")
            return HttpResponseRedirect('/dashboard/')
        return render(request, "login/login_error.html", {'login': log_in})

    return render(request, 'login/login.html', {'login': log_in})