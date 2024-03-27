from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField(validators=[MinValueValidator(0)])
    stock=models.IntegerField(validators=[MinValueValidator(0)])
    ing_url=models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class offer(models.Model):
    code=models.CharField(max_length=10)
    discount=models.FloatField()
    description=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name



    