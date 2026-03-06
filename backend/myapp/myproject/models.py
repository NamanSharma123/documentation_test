from django.db import models

# Create your models here.
class Product(models.Model):
    stockkeeping_unit = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description  = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return (f"{self.name} ({self.stockkeeping_unit}) - ${self.price}")
