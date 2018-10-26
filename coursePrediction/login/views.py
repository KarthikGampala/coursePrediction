# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .forms import UserForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def login_user(request):
    flag = 0
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and flag == 0:
                login(request, user)
                flag = 1
                #return render(request, 'index.html')
                return HttpResponse('logged in')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


"""def signup(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user  = form.save(commit=False)
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password']
        check = form.cleaned_data['password1']
        if(check != raw_password):
        	return HttpResponse("Check ur password properly bitch")
        user.set_password(raw_password)
        user.save()
        user = authenticate(username=username, password=raw_password)
        if user is not None:
        	if user.is_active:
        		login(request, user)
        		return HttpResponse("Registered u bitch")
        return redirect('signup')

	return render(request, 'signup.html', {"form": form })"""

def logout_view(request):
    logout(request)
    return HttpResponse('logged out')