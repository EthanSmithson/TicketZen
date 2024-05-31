from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tickets/', views.about, name='tickets'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('check_username/', views.check_username, name='check_username'),
    path('check_email/', views.check_email, name='check_email'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
]