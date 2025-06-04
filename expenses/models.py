from django.db import models

# Create your models here.

class Income(models.Model):
    source = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date_received = models.DateField()

    def __str__(self):
        return f"{self.source} - ₦{self.amount}"

class Expense(models.Model):
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date_spent = models.DateField()

    def __str__(self):
        return f"{self.category} - ₦{self.amount}"
