from django.db import models

# Create your models here.

class Payment(models.Model):
    cod = models.BooleanField()
    debit = models.BooleanField()
    credit = models.BooleanField()
    emi = models.BooleanField()
