from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import forms

app_name = 'account'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html', form_class=forms.UserLoginForm), name='login'),
	path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
	path('register/', views.user_registration_view, name='register'),
	path('delete/', views.user_deletion_view, name='delete'),
	path('delete/confirm/', views.user_deletion_confirm, name='delete_confirm'),
	path('users/', views.index_view, name='index'),
	path('users/<int:pk>/', views.detail_view, name='detail'),
]
