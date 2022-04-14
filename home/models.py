from django.db import models

# Create your models here.

class login(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    class Meta:
        db_table : 'basic'