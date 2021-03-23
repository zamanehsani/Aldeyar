
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
    path('salary', dash_view.Salary.as_view(), name="salary"),
    path('pay-salary', dash_view.Pay_salary.as_view(), name="pay_salary"),
    path('salary/<int:pk>/update', dash_view.Update_salary.as_view(), name="update_salary"),
    path('salary/<int:pk>/delete', dash_view.Delete_Salary.as_view(), name="delete_salary"),
]
