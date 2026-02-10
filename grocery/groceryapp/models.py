from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    weight = models.CharField(max_length=100)
    image = models.ImageField(upload_to='grocery_image', null=True)


    def __str__(self):
        return self.name