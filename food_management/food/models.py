from django.db import models

# Create your models here.
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.quantity} - {self.expiration_date}"

    # Optionally, add a method to check if the food is expired
    def is_expired(self):
        from datetime import date
        return self.expiration_date < date.today()
