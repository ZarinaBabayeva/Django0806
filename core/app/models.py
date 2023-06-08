from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
