from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from .forms import UserCreation
from .models import UserProfile

# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        user_form = UserCreation(data=request.POST)
        if user_form.is_valid():
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            height = request.POST['height']
            weight = request.POST['weight']
            age = request.POST['age']
            sex = request.POST['sex']
            excercise = request.POST['excercise']
            diet = request.POST['diet']
            bmi = (weight/height**2)*703
            if User.objects.filter(email = email).exists():
                return render(request,'signup/signup_error.html', {"ucreation": UserCreation, "error": "Email Already Exists!"})
            if User.objects.filter(username = username).exists():
                return render(request,'signup/signup_error.html', {"ucreation": UserCreation, "error": "Username Already Exists!"})
            else:
                # saving user for login info
                user = User.objects.create_user(email=email, username=username, password=password)
                user.set_password(password)
                user.save()
                # creating a userprofile
                userp = UserProfile(email = email, username = username, password = password, height=height, weight=weight, age=age, excercise=excercise, diet=diet, bmi=bmi, sex=sex)
                userp.save()
                u = User.objects.get(email=email)
                user = authenticate(username=u.get_username(),password=password)
                login(request, user)
                return HttpResponseRedirect('dashboard')

    return render(request, 'signup/signup.html', {"form": UserCreation})
