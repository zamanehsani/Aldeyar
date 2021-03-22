from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'index.html')
# Create your views here.

def dasboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form = UserCreationForm()
        data = {'form': form}

    return render(request,'register.html', data)