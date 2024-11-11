from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('transfer/', views.transfer_money, name='transfer'),
    path('send-money/', views.send_money, name='send_money'),
    path('pay-utilities/', views.pay_utilities, name='pay_utilities'),
    path('book-ticket/', views.book_ticket, name='book_ticket'),
    path('cinema/', views.book_cinema, name='cinema'),
    path('bus-fare/', views.pay_bus_fare, name='bus_fare'),
    path('savings/', views.savings, name='savings'),
]