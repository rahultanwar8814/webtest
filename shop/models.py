from django.db import models

# Create your models here.
from django.db import models

class item(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.name

