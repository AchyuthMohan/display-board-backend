from pyexpat import model
from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField((""))
    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)

    
    