# -*- coding: utf-8 -*-
from django.db import models
from  django.contrib.auth.models import User
import random, datetime


class Who(models.Model):
    class Meta:
        db_table = 'who'

    who_is_who = models.CharField(max_length=255)

    def __unicode__(self):
        return self.who_is_who


class Profile(models.Model):
    class Meta:
        db_table = "profile"


    user_id = models.ForeignKey(User)
    user_id_doctor = models.ForeignKey(User, related_name="doctor")
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_who = models.ForeignKey(Who, default=0, blank=True, verbose_name=u"Кто ты?")

    def __unicode__(self):
        return self.first_name + " " + self.second_name + " " + self.last_name



class PotientList(models.Model):

    class Meta():
        db_table = "potientList"


    add_user_id = models.ForeignKey(Profile, related_name="Doctor", verbose_name=u"Добавил врач")
    patient_user_id = models.ForeignKey(Profile, related_name="Patient", verbose_name=u"Больной")
    add_date = models.DateTimeField()

    diagnoz = models.TextField(blank=True)
    vypiska = models.BooleanField(blank=True, default=False)
    obj_3d = models.FileField(blank=True, upload_to="/media/obj3d/", default="")

# Create your models here.


