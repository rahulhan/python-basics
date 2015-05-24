from django.db import models
from django.contrib.auth.models import User


class Details(models.Model):
    '''
        User details model
    '''
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=50)
    user = models.OneToOneField(User)

    class Meta:
        ordering = ['user']
        verbose_name_plural = "Details"
