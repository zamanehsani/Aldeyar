from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Dash import models
from django.contrib.auth.models import User
from Dash.forms import UserUpdate


def index(request):
    return render(request,'index.html')
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

class Profile(DetailView):
    model = User
    template_name = 'profile.html'

    def post(self, request, pk):
        user = User.objects.get(pk = request.user.id)
        form = UserUpdate(request.POST, instance=user)
        if form.is_valid():
            form.save()
            
            return redirect('profile', pk=user.id)
        return redirect('profile', pk=user.id)

class Update_profile(LoginRequiredMixin,UpdateView):
    login_url = '/login'
    model = User
    template_name = 'user_form.html'
    fields = ['first_name', 'last_name', 'email','username']
    success_url = ''
    def get_context_data(self, *args, **kwargs):
        data = super(Update_profile, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Update Profile'
        return data

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

# Sales
class Sale(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = models.Sale
    template_name = "sale.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Sale, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Sales'
        return data

class Add_sale(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = models.Sale
    template_name = 'sale_form.html'
    fields = ['bread', 'quantity', 'cleint']

    def get_context_data(self, *args, **kwargs):
        data = super(Add_sale, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Sales From'
        return data
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Update_sale(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login'
    model = models.Sale
    template_name = 'sale_form.html'
    fields = ['bread', 'quantity', 'cleint']

    def get_context_data(self, *args, **kwargs):
        data = super(Update_sale, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Sales'
        return data

    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False

class Delete_sale(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = models.Sale
    template_name = "delete_sale.html"
    success_url = '/sale'

    def get_context_data(self, *args, **kwargs):
        data = super(Delete_sale, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Sales'
        return data
    
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False


# Bread
class Bread(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = models.Bread
    template_name = "bread.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Bread, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Bread Pack'
        return data

class Add_bread(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = models.Bread
    template_name = 'bread_form.html'
    fields = ['package', 'price']

    def get_context_data(self, *args, **kwargs):
        data = super(Add_bread, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Bread From'
        return data

class Update_bread(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = models.Bread
    template_name = 'bread_form.html'
    fields = ['package', 'price']

    def get_context_data(self, *args, **kwargs):
        data = super(Update_bread, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Bread'
        return data
    

class Delete_bread(LoginRequiredMixin, DeleteView):
    model = models.Bread
    template_name = "delete_bread.html"
    success_url = '/bread'

    def get_context_data(self, *args, **kwargs):
        data = super(Delete_bread, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Bread'
        return data

# the Rent, 
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
    