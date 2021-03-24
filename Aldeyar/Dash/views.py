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

# the staff expenses, 
class Rent(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = models.Rent
    template_name = "rent.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Rent, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Rent'
        return data

class Add_rent(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = models.Rent
    template_name = 'rent_form.html'
    fields = ['rent', 'month', 'Pay']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Update_rent(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login'
    model = models.Rent
    template_name = 'rent_form.html'
    fields = ['rent', 'month', 'Pay']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False

class Delete_rent(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Rent
    template_name = "delete_rent.html"
    success_url = '/rent'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_rent, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Rent'
        return data
    
    # to check if the user is the same who created to delete 
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False


# the staff expenses, 
class Staff_expense(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = models.Staff_Expenses
    template_name = "staff_expense.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Staff_expense, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Staff Expense'
        return data

class Add_staff_expense(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = models.Staff_Expenses
    template_name = 'staff_expense_form.html'
    fields = ['name', 'totol_price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Update_staff_expense(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login'
    model = models.Staff_Expenses
    template_name = 'staff_expense_form.html'
    fields = ['name', 'totol_price']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False

class Delete_staff_expense(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Staff_Expenses
    template_name = "delete_staff_expense.html"
    success_url = '/staff-expense'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_staff_expense, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Staff Expense'
        return data
    
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False

# the expenses, 
class Expense(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = models.Expenses
    template_name = "expense.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Expense, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Expenses'
        return data

class Add_expense(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = models.Expenses
    template_name = 'expense_form.html'
    fields = ['name', 'quantity', 'unit_type', 'Unit_price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.totol_price = form.instance.quantity * form.instance.Unit_price
        return super().form_valid(form)

class Update_expense(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login'
    model = models.Expenses
    template_name = 'expense_form.html'
    fields = ['name', 'quantity', 'unit_type', 'Unit_price']
    
    def form_valid(self, form):
        form.instance.pay_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False

class Delete_expense(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Expenses
    template_name = "delete_expense.html"
    success_url = '/expense'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_expense, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Expense'
        return data
    
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False
    

# the salary module includes the listing, making the payment, removal and editing
class Salary(LoginRequiredMixin, ListView):
    model = models.Staff_Salary
    template_name = "salary.html"
    login_url = '/login'

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
    