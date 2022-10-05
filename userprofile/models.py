from django.db import models
from django.contrib.auth.models import User
from .conts import ChoicePlans


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        related_name='profile',
        on_delete=models.CASCADE,
    )
    plan = models.CharField(
        max_length=15,
        choices=ChoicePlans.CHOICE_PLANS,
        default=ChoicePlans.BASIC
    )

    def __str__(self):
        return f'{self.user}-{self.plan}'
