from django.contrib import admin
from django.contrib import auth
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user'),
    path('account/', views.accSettings, name='account'),


    path('', views.home, name='home'),
    
    path('products/', views.products,name='products' ),
    path('customer/<str:pk>/', views.customer, name='customer'),
    
    path('create_order/<str:pk_k>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
    
    path('pw_reset', 
    auth_views.PasswordResetView.as_view(template_name="accounts/pw_reset.html"),
     name='pw_reset'),
    path('pw_reset_sent', auth_views.PasswordResetDoneView.as_view(template_name="accounts/pw_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/pw_reset_confirm.html"), name='password_reset_confirm'),
    path('pw_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/pw_reset_complete.html"),name='password_reset_complete'),
    
     
]

'''
Submit email form   //PasswordResetView.as_view()
Email Sent for pw change    //PasswordResetDoneView.as_view()
Link to password reset form in email    //PasswordResetConfirmView.as_view()
Password successfully changed msg   //PasswordResetCompleteView.as_view()

'''