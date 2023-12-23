from django.db import models

# Create your models here.

class Emp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    phone_number= models.IntegerField(default=0)

    def __str__(self):
        return self.first_name

    

