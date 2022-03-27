from unicodedata import name
from django.shortcuts import render

from signup.models import UserProfile

# Create your views here.


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
