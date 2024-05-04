from django.db import models

# Create your models here.
class Menu(models.Model):
    image = models.ImageField(upload_to='menu_images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
