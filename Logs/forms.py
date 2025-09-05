from django import forms
from .models import Medicine, PurchaseLog
import calendar
from datetime import datetime

class NewMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'name',
            'price_per_unit',
            'morning_dose',
            'lunch_dose',
            'dinner_dose',
            'morning_timing',
            'lunch_timing',
            'dinner_timing',
            'notes'
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
            'morning_timing': forms.Select(),
            'lunch_timing': forms.Select(),
            'dinner_timing': forms.Select(),
        }

class PurchaseExistingForm(forms.ModelForm):
    class Meta:
        model = PurchaseLog
        fields = ['medicine', 'bought_quantity', 'price_per_unit']
        widgets = {
            'medicine': forms.Select(),  # Dropdown of existing medicines
        }

class MonthlyCostForm(forms.Form):
    year = forms.IntegerField(
        min_value=2000,  # Adjust as needed
        max_value=datetime.now().year + 1,
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'YYYY'})
    )
    month = forms.ChoiceField(
        choices=[(i, calendar.month_name[i]) for i in range(1, 13)],
        required=True
    )