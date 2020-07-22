from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [


	path('register/', views.register_page, name="register"),
	path('login/', views.login_page, name='login'),
	path('account/', views.account_settings, name='account'),
	path('logout/', views.logout_page, name='logout'),
	path('user/', views.userPage, name='user-page'),
    path('', views.home, name='home'), 

    path('products/', views.products, name = 'products'),

    path('customers/<str:pk>/', views.customers, name='customer'),

    path('create_order/<str:pk>/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),

    path('reset_password/', 
    	auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"),
    	 name="reset_password"),

    path('reset_password_done/', 
	    	auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_done.html"),
	    	 name="password_reset_done"),


    path('reset_password_confirm/<uidb64>/<token>/', 
	    	auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password_confirm.html"),
	    	 name="password_reset_confirm"),


    path('reset_password_complete/',
	     auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password_complete.html"), 
	     name="password_reset_complete")





  ]