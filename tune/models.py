from django.db import models
from django.urls import reverse

# Create your models here.

class Tune(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=4)
    fiddler = models.CharField(max_length=100)
    tuning = models.CharField(max_length=4)
    state = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    stars = models.IntegerField()

    
    def __str__(self) -> str:
        return f'{self.name} {self.id}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tune_id': self.id})
