from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, help_text="Default price per unit")
    morning_dose = models.IntegerField(default=0, help_text="Dose for morning (e.g., number of pills)")
    lunch_dose = models.IntegerField(default=0, help_text="Dose for lunch (e.g., number of pills)")
    dinner_dose = models.IntegerField(default=0, help_text="Dose for dinner (e.g., number of pills)")
    morning_timing = models.CharField(
        max_length=10,
        choices=[('before', 'Before Meal'), ('after', 'After Meal')],
        default='after',
        help_text="Timing for morning dose"
    )
    lunch_timing = models.CharField(
        max_length=10,
        choices=[('before', 'Before Meal'), ('after', 'After Meal')],
        default='after',
        help_text="Timing for lunch dose"
    )
    dinner_timing = models.CharField(
        max_length=10,
        choices=[('before', 'Before Meal'), ('after', 'After Meal')],
        default='after',
        help_text="Timing for dinner dose"
    )
    available_quantity = models.IntegerField(default=0, help_text="Current available quantity (auto-updated)")
    notes = models.TextField(blank=True, help_text="Any additional notes")

    def __str__(self):
        return self.name

class PurchaseLog(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='purchases')
    bought_quantity = models.IntegerField(help_text="Quantity bought in this purchase")
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit for this purchase")
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine.name} - {self.bought_quantity} on {self.purchase_date}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Auto-update available quantity
        self.medicine.available_quantity += self.bought_quantity
        self.medicine.save()