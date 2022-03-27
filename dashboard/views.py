from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import numpy as np

import pandas as pd

# Models
from signup.models import UserProfile

# Helper Functions


def weight_percentile(age, sex, value):
    if sex == 'female':
        if age == 13:
            mean, stderr = 125.8, 3.72
        if age == 14:
            mean, stderr = 137.0, 2.19
        if age == 15:
            mean, stderr = 137.5, 3.36
        if age == 16:
            mean, stderr = 144.9, 3.57
        if age == 17:
            mean, stderr = 149.7, 3.57
        if age == 18:
            mean, stderr = 151.6, 3.70
        if age == 19:
            mean, stderr = 156.5, 4.37
        if age in range(20, 30):
            mean, stderr = 165.0, 2.49
        if age in range(30, 40):
            mean, stderr = 174.9, 2.19
        if age in range(40, 50):
            mean, stderr = 178.1, 3.14
        if age in range(50, 60):
            mean, stderr = 173.5, 2.23
        if age in range(60, 70):
            mean, stderr = 173.5, 2.23
        if age in range(60, 70):
            mean, stderr = 172.4, 2.68
        if age in range(70, 80):
            mean, stderr = 164.6, 2.10
        if age > 80:
            mean, stderr = 149.7, 2.22
    elif sex == 'male':
        if age == 13:
            mean, stderr = 133.2, 3.33
        if age == 14:
            mean, stderr = 143.6, 3.88
        if age == 15:
            mean, stderr = 160.2, 4.25
        if age == 16:
            mean, stderr = 157.2, 3.37
        if age == 17:
            mean, stderr = 170.0, 4.16
        if age == 18:
            mean, stderr = 166.7, 4.34
        if age == 19:
            mean, stderr = 176.2, 3.59
        if age in range(20, 30):
            mean, stderr = 188.6, 3.17
        if age in range(30, 40):
            mean, stderr = 208.1, 2.68
        if age in range(40, 50):
            mean, stderr = 206.9, 2.29
        if age in range(50, 60):
            mean, stderr = 202.5, 2.48
        if age in range(60, 70):
            mean, stderr = 201.2, 1.80
        if age in range(60, 70):
            mean, stderr = 193.4, 2.39
        if age in range(70, 80):
            mean, stderr = 80.5, 0.90
        if age > 80:
            mean, stderr = 177.5, 1.98
    sim_distr = np.random.normal(mean, stderr, 10000)
    return np.percentile(sim_distr, value)


def bmi_percentile(age, sex, value):
    if sex == 'female':
        if age == 13:
            mean, stderr = 22.7, 0.54
        if age == 14:
            mean, stderr = 23.7, 0.39
        if age == 15:
            mean, stderr = 24.0, 0.55
        if age == 16:
            mean, stderr = 25.0, 0.56
        if age == 17:
            mean, stderr = 25.6, 0.65
        if age == 18:
            mean, stderr = 26.1, 0.66
        if age == 19:
            mean, stderr = 26.9, 0.82
        if age in range(20, 30):
            mean, stderr = 29.8, 0.24
        if age in range(30, 40):
            mean, stderr = 28.3, 0.45
        if age in range(40, 50):
            mean, stderr = 29.9, 0.32
        if age in range(50, 60):
            mean, stderr = 30.7, 0.51
        if age in range(60, 70):
            mean, stderr = 30.3, 0.41
        if age in range(60, 70):
            mean, stderr = 30.3, 0.47
        if age in range(70, 80):
            mean, stderr = 29.8, 0.37
        if age > 80:
            mean, stderr = 28.0, 0.37
    elif sex == 'male':
        if age == 13:
            mean, stderr = 22.7, 0.48
        if age == 14:
            mean, stderr = 22.5, 0.47
        if age == 15:
            mean, stderr = 24.4, 0.67
        if age == 16:
            mean, stderr = 23.6, 0.44
        if age == 17:
            mean, stderr = 25.1, 0.63
        if age == 18:
            mean, stderr = 24.7, 0.68
        if age == 19:
            mean, stderr = 26.1, 0.63
        if age in range(20, 30):
            mean, stderr = 29.4, 0.19
        if age in range(30, 40):
            mean, stderr = 27.6, 0.43
        if age in range(40, 50):
            mean, stderr = 30.3, 0.39
        if age in range(50, 60):
            mean, stderr = 30.1, 0.32
        if age in range(60, 70):
            mean, stderr = 29.8, 0.34
        if age in range(60, 70):
            mean, stderr = 29.9, 0.23
        if age in range(70, 80):
            mean, stderr = 29.2, 0.31
        if age > 80:
            mean, stderr = 27.6, 0.23
    sim_distr = np.random.normal(mean, stderr, 10000)
    return np.percentile(sim_distr, value)

# Render Requests


@login_required(login_url='/login/')
def dashboard(request):
    user = UserProfile.objects.get(username=request.user)
    data = {
        'name': user.username,
        'height': user.height,
        'weight': user.weight,
        'age': user.age,
        'excercise': user.excercise,
        'diet': user.diet,
    }
    return render(request, 'dashboard/dashboard.html', data)


@login_required(login_url='/login/')
def resources(request):
    user = UserProfile.objects.get(username=request.user)
    data = {
        'name': user.username,
        'height': user.height,
        'weight': user.weight,
        'age': user.age,
        'excercise': user.excercise,
        'diet': user.diet,
        'weight_percentile': weight_percentile(user.age, user.sex, user.weight),
        'bmi_percentile': bmi_percentile(user.age, user.sex, user.bmi),
    }

    return render(request, 'dashboard/resources.html', data)


@login_required(login_url='/login/')
def settings(request):
    user = UserProfile.objects.get(username=request.user)
    data = {
        'name': user.username,
        'height': user.height,
        'weight': user.weight,
        'age': user.age,
        'excercise': user.excercise,
        'diet': user.diet,
    }
    return render(request, 'dashboard/settings.html', data)


@login_required(login_url='/login/')
def about(request):
    user = UserProfile.objects.get(username=request.user)
    data = {
        'name': user.username,
        'height': user.height,
        'weight': user.weight,
        'age': user.age,
        'excercise': user.excercise,
        'diet': user.diet,
    }
    return render(request, 'dashboard/about.html', data)

# API Endpoint


def get_weight(request):
    if request.method == 'GET':
        weight = [200, 201, 200.5, 199, 200]
        weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
        response = {
            "weight": weight,
            "weeks": weeks
        }
        return JsonResponse(response, status=200)
    return JsonResponse({"error": "Something went wrong"}, status=400)


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
