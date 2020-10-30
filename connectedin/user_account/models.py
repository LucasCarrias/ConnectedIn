from django.db import models
from django.contrib.auth.models import User


class UserAccount(User):
    birth_date = models.DateField(blank=True, null=True)