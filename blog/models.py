from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Order(models.Model):
    order_id = models.CharField(max_length=100)

    total_amount = models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.status








