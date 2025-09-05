from django.db import models

class MedicineLog(models.Model):
    medicine_name = models.CharField(max_length=200)
    available_quantity = models.IntegerField(help_text="Current available quantity")
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, help_text="Bought price per unit")
    bought_quantity = models.IntegerField(help_text="Quantity bought in this purchase")
    morning_dose = models.IntegerField(default=0, help_text="Dose for morning (e.g., number of pills)")
    lunch_dose = models.IntegerField(default=0, help_text="Dose for lunch (e.g., number of pills)")
    dinner_dose = models.IntegerField(default=0, help_text="Dose for dinner (e.g., number of pills)")
    timing = models.CharField(
        max_length=10,
        choices=[('before', 'Before Meal'), ('after', 'After Meal')],
        default='after',
        help_text="Take before or after meals"
    )
    purchase_date = models.DateField(auto_now_add=True, help_text="Date of purchase/log entry")
    notes = models.TextField(blank=True, help_text="Any additional notes")

    def __str__(self):
        return f"{self.medicine_name} - {self.purchase_date}"