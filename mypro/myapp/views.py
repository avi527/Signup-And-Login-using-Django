from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
# from myapp.decorators import admin_only
from django.contrib.auth.decorators import login_required
def home(request):
	return HttpResponse("Hello ORM Relationship")
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #print(user)
        if user:
            login(request, user)
            return redirect('user_success')
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "register.html", context)
    else:
        return render(request, "register.html", context)
	# return render(request,'accounts/register.html')
@login_required(login_url="user_login")
def user_success(request):
    context = {}
    context['user'] = request.user
    return render(request, "success.html", context)
def user_logout(request):
    logout(request)
    return redirect('user_login')
@login_required(login_url="user_login") 
def Customer(request):
	return render(request,'accounts/customer.html')
def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})

