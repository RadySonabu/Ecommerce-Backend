from django.db import models
from ..base.models import BaseModel
import uuid
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    id =  models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gcash_number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'