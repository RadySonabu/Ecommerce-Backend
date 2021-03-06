from django.db import models
from ..base.models import BaseModel
# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='media')
    description = models.CharField(max_length=50)
    quantity = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name
    