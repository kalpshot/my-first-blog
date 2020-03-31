from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    Owner_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Pet_name = models.CharField(max_length=200)
    Breed = models.CharField(max_length=200)
    Date_of_birth = models.DateTimeField(default=timezone.now)




    def __str__(self):
        return self.Pet_name

# Create your models here.
