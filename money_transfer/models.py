from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    mobile_number = models.CharField(max_length=20)
    mobile_money_provider = models.CharField(max_length=50)
    mobile_money_account_id = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='money_transfer_users',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='money_transfer_users',
    )

class Transfer(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transfers')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transfers')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)

class Savings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    recurring = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)