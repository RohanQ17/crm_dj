from django.db import models

class CRM(models.Model):
    recorded_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)

    def __str__(self):
         return(f"{self.name}")
