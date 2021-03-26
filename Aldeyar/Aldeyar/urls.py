
from django.contrib import admin
from django.urls import path, reverse_lazy
from Dash import views as dash_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dash_view.index, name='index'),
    path('dashboard', dash_view.dashboard, name='dashboard'),
    path('login', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name="index.html"), name="logout"),
    # password reset
    path('password-reset', 
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
        name="password_reset"),

    path('password-reset-done', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>', 
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html", success_url=reverse_lazy('password_has_reset')), 
        name="password_reset_confirm"),
    
    # this is view is not some how not loading. so the connfirm path with redireect to pass done function
    path('password-reset-complete', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_complete.html"), 
        name="password_reset_complete"),
    
    # after the password redirect (this function as the password reset complete page)
    path('password-has-reset', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_complete.html"), 
        name="password_has_reset"),

    # profile
    path('profile/<int:pk>', dash_view.Profile.as_view(), name="profile"),
    path('profile/<int:pk>/u/pdate', dash_view.Update_profile.as_view(), name="update_profile"),

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
    # Bread
    path('bread', dash_view.Bread.as_view(), name="bread"),
    path('add-bread', dash_view.Add_bread.as_view(), name="add_bread"),
    path('bread/<int:pk>/update', dash_view.Update_bread.as_view(), name="update_bread"),
    path('bread/<int:pk>/delete', dash_view.Delete_bread.as_view(), name="delete_bread"),
    # Sakes Order
    path('sale', dash_view.Sale.as_view(), name="sale"),
    path('add-sale', dash_view.Add_sale.as_view(), name="add_sale"),
    path('sale/<int:pk>/update', dash_view.Update_sale.as_view(), name="update_sale"),
    path('sale/<int:pk>/delete', dash_view.Delete_sale.as_view(), name="delete_sale"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
