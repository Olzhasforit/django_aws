from django.db import models

class Bucket(models.Model):
    name = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    file = models.FileField(null=True, blank=True)

