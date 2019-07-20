from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import (
    LoginView,
    RegistrationView,
    PasswordResetView
)
app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', success_url='/accounts/password_reset/done'), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(success_url='/accounts/reset/done'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]