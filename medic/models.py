from django.db import models
from  django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        db_table = "userProfile"

    firstName = models.CharField(max_length=200)
    secondName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200, blank=True)

    user_id = models.ForeignKey(User)

class Doctor (models.Model):
    class Meta:
        db_table = "doctor"

    user_profile_id = models.ForeignKey(UserProfile)
    zvanie = models.CharField(max_length=300)


class Patient (models.Model):
    class Meta:
        db_table = "patient"

    user_profile_id = models.ForeignKey(UserProfile)
    diagnoz = models.TextField()
    model3d = models.TextField()


# Create your models here.
