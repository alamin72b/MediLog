from django.shortcuts import render, redirect
from .models import Medicine, PurchaseLog
from .forms import NewMedicineForm, PurchaseExistingForm, MonthlyCostForm
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Sum, F

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'Logs/medicine_list.html', {'medicines': medicines})

def new_medicine_create(request):
    if request.method == 'POST':
        form = NewMedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = NewMedicineForm()
    return render(request, 'Logs/new_medicine_create.html', {'form': form})

def purchase_existing_create(request):
    if request.method == 'POST':
        form = PurchaseExistingForm(request.POST)
        if form.is_valid():
            form.save()  # This triggers the auto-update in model save()
            return redirect('medicine_list')
    else:
        form = PurchaseExistingForm()
    return render(request, 'Logs/purchase_existing_create.html', {'form': form})

def monthly_cost(request):
    form = MonthlyCostForm(request.GET or None)  # Use GET for simplicity (no CSRF needed for read-only)
    year = None
    month = None
    total_cost = 0
    purchases = PurchaseLog.objects.none()
    selected_month = "Previous Month"  # Default label

    if form.is_valid():
        year = form.cleaned_data['year']
        month = form.cleaned_data['month']
    else:
        # Default to previous month
        today = datetime.today()
        prev_month = today - relativedelta(months=1)
        year = prev_month.year
        month = prev_month.month

    if year and month:
        first_day = datetime(year, int(month), 1)
        last_day = first_day + relativedelta(months=1) - relativedelta(days=1)
        selected_month = f"{calendar.month_name[int(month)]} {year}"

        purchases = PurchaseLog.objects.filter(
            purchase_date__range=(first_day, last_day)
        )
        total_cost = purchases.aggregate(
            total=Sum(F('bought_quantity') * F('price_per_unit'))
        )['total'] or 0

    context = {
        'form': form,
        'total_cost': total_cost,
        'month': selected_month,
        'purchases': purchases
    }
    return render(request, 'Logs/monthly_cost.html', context)