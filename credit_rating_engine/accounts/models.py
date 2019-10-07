from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    hashed_nin              = models.CharField(max_length=64, unique=True)
    bnu_address             = models.CharField(max_length=108)
    spendp_key              = models.CharField(max_length=64, null=True, blank=True)
    spendpr_key             = models.CharField(max_length=64, null=True, blank=True)
    physical_address        = models.CharField(max_length=255)
    user_number             = models.CharField(max_length=255)
    refferal_id             = models.CharField(max_length=6)
    role                    = models.IntegerField(null=True, blank=True)
