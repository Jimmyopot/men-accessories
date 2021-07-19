from django.db import models


CATEGORY_CHOICES = (
    ('O', 'Official'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear'),
    ('C', 'Casual'),
    ('I', 'Indoors'),
)

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default="")
    description = models.TextField(default="This is a product description")
    image = models.ImageField(blank=True, null=True, upload_to = "images/")
    
    def __str__(self):
        return self.title
    
    
class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name