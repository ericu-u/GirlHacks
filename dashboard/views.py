from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Models
from signup.models import UserProfile


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
        weight = [170, 178, 171, 167, 170, 171, 165]
        weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7"]
        response = {
            "data": weight,
            "weeks": weeks
        }
        return JsonResponse(response, status=200)
    return JsonResponse({"error": "Something went wrong"}, status=400)

def get_height(request):
    if request.method == 'GET':
        height = [170, 178, 171, 167, 170, 171, 165]
        weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7"]
        response = {
            "data": height,
            "weeks": weeks
        }
        return JsonResponse(response, status=200)
    return JsonResponse({"error": "Something went wrong"}, status=400)

def get_BMI(request):
    if request.method == 'GET':
        bmi = [26.5, 26.4, 27.1, 26.9, 24.8, 26.3, 26.1]
        weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7"]
        response = {
            "data": bmi,
            "weeks": weeks
        }
        return JsonResponse(response, status=200)
    return JsonResponse({"error": "Something went wrong"}, status=400)

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')