from django.urls import path
from . import views

urlpatterns = [
    path('incomes/', views.income_list, name='income_list'),
    path('incomes/add/', views.add_income, name='add_income'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add/', views.add_expense, name='add_expense'),
]
