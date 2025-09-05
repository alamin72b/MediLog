from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicine_list, name='medicine_list'),
    path('new/', views.new_medicine_create, name='new_medicine_create'),
    path('purchase/', views.purchase_existing_create, name='purchase_existing_create'),
    path('monthly-cost/', views.monthly_cost, name='monthly_cost'),
]