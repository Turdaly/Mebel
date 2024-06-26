from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Categoria(models.Model):
    type = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return str(self.type)

class Jihaz(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    width = models.PositiveIntegerField(null=False, blank=False)
    height = models.PositiveIntegerField(null=False, blank=False)
    deep = models.PositiveIntegerField(default=0, null=False, blank=False)
    material = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(default='default.jpg', null=False, blank=False)
    
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("jihaz_detail", kwargs={"pk": self.pk})
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jihaz = models.ForeignKey(Jihaz, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    


    