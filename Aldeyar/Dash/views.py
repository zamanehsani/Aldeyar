from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Dash import models


def index(request):
    return render(request,'index.html')
# Create your views here.

def dashboard(request):
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

class Salary(LoginRequiredMixin, ListView):
    model = models.Staff_Salary
    template_name = "salary.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Salary, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Employee Salary'
        return data


class Pay_salary(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = models.Staff_Salary
    template_name = 'staff_salary_form.html'
    fields = ['name', 'salary', 'month', 'Pay']
    
    def form_valid(self, form):
        form.instance.pay_by = self.request.user
        return super().form_valid(form)


class Update_salary(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login'
    model = models.Staff_Salary
    template_name = 'staff_salary_form.html'
    fields = ['name', 'salary', 'month', 'Pay']
    
    def form_valid(self, form):
        form.instance.pay_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        salary = self.get_object()
        if self.request.user == salary.pay_by:
            return True
        return False

class Delete_Salary(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Staff_Salary
    template_name = "delete_salary.html"
    success_url = '/salary'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_Salary, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Employee Salary'
        return data
    
    def test_func(self):
        salary = self.get_object()
        if self.request.user == salary.pay_by:
            return True
        return False
    