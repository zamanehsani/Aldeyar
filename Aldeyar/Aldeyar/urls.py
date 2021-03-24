
from django.contrib import admin
from django.urls import path
from Dash import views as dash_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dash_view.index, name='index'),
    path('dashboard', dash_view.dashboard, name='dashboard'),
    path('login', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name="index.html"), name="logout"),
    path('profile', dash_view.profile, name="profile"),
    path('register', dash_view.register, name="register"),
    # listing the urls for salary 
    path('salary', dash_view.Salary.as_view(), name="salary"),
    path('pay-salary', dash_view.Pay_salary.as_view(), name="pay_salary"),
    path('salary/<int:pk>/update', dash_view.Update_salary.as_view(), name="update_salary"),
    path('salary/<int:pk>/delete', dash_view.Delete_Salary.as_view(), name="delete_salary"),
    # listing the urls for Expenses
    path('expense', dash_view.Expense.as_view(), name="expense"),
    path('add-expense', dash_view.Add_expense.as_view(), name="add_expense"),
    path('expense/<int:pk>/update', dash_view.Update_expense.as_view(), name="update_expense"),
    path('expense/<int:pk>/delete', dash_view.Delete_expense.as_view(), name="delete_expense"),
    # listing the urls for  Staff Expenses
    path('staff-expense', dash_view.Staff_expense.as_view(), name="staff_expense"),
    path('add-staff-expense', dash_view.Add_staff_expense.as_view(), name="add_staff_expense"),
    path('staff-expense/<int:pk>/update', dash_view.Update_staff_expense.as_view(), name="update_staff_expense"),
    path('staff-expense/<int:pk>/delete', dash_view.Delete_staff_expense.as_view(), name="delete_staff_expense"),
    # Rent
    path('rent', dash_view.Rent.as_view(), name="rent"),
    path('add-rent', dash_view.Add_rent.as_view(), name="add_rent"),
    path('rent/<int:pk>/update', dash_view.Update_rent.as_view(), name="update_rent"),
    path('rent/<int:pk>/delete', dash_view.Delete_rent.as_view(), name="delete_rent"),

]
