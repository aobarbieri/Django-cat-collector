from django.db import models
from django.urls import reverse

# Create your models here.
# Used to perform CRUD database operations in Django -> Python class that inherits from models.Model
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})