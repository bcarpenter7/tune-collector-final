from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from account.models import MyUser


# Create your models here.

class Tune(models.Model):
    KEY_CHOICES = (
        ('A', 'A'),
        ('C', 'C'),
        ('D', 'D'),
        ('G', 'G'),
        ('F', 'F'),
    )
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=1, choices=KEY_CHOICES)
    fiddler = models.CharField(max_length=100, null=True, blank=True)
    tuning = models.CharField(max_length=4, default='GDAE')
    state = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='tunes', blank=True)

    def __str__(self) -> str:
        return f'{self.name} {self.id}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tune_id': self.id})
