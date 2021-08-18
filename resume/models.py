from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 1000)
    text = models.CharField(max_length = 10000)
    email = models.EmailField()
    message = models.TextField()