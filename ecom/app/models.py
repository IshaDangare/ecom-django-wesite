from django.db import models
from django.contrib.auth.models import User

class CustomManager(models.Manager):
    def get_price_range(self,r1,r2):
        return self.filter(price__range=(r1,r2))
    
    def get_mobile_list(self):
        return self.filter(category__exact="Carrara")
    def get_clothes_list(self):
        return self.filter(category__exact="Statuary")
    def get_shoes_list(self):
        return self.filter(category__exact="Calacatta")
    def get_mobile_list(self):
        return self.filter(category__exact="Emperador")
    def get_mobile_list(self):
        return self.filter(category__exact="Crema Marfil")
    
# Create your models here.
class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length=50)
    pro_desc = models.CharField(max_length=50)
    pro_img = models.ImageField(upload_to='img')
    pro_price = models.IntegerField(max_length=50)

    # Use CharField for pro_cat instead of ChoiceField
    choices = [
        ('Carrara', 'Carrara'), 
        ('Statuary', 'Statuary'), 
        ('Calacatta', 'Calacatta'), 
        ('Emperador', 'Emperador'), 
        ('Crema Marfil', 'Crema Marfil')
    ]
    pro_cat = models.CharField(max_length=30, choices=choices)  # Use CharField for pro_cat
    objects = models.Manager()
    prod = CustomManager()