from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tickets/', views.tickets, name='tickets'),
    # path('findTickets/', views.findTickets, name='findTickets'),
    path('home/', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('check_username/', views.check_username, name='check_username'),
    path('check_email/', views.check_email, name='check_email'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    path('origin_airport_search/', views.origin_airport_search, name='origin_airport_search'),
    path('destination_airport_search/', views.destination_airport_search, name='destination_airport_search'),
    path('book_flight/<str:flight>/', views.book_flight, name='book_flight'),
    path('demo/', views.demo, name='demo'),
]