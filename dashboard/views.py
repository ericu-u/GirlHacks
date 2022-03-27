from django.shortcuts import render
from django.http import JsonResponse

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