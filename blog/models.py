from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    da = models.DateField(auto_now_add=True)
    