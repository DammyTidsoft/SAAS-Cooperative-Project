from django.shortcuts import render, redirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm


# Create your views here.

def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'finance/income_list.html', {'incomes': incomes})

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'finance/add_income.html', {'form': form})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'finance/expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'finance/add_expense.html', {'form': form})
