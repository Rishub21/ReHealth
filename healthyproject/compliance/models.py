from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField #json field allows us to essentially store as a dictionary attribute


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length = 100, default = "")
    password = models.CharField(max_length = 100, default = "")
    specialty = models.CharField(max_length = 100, default = "")
    Patient_list = JSONField(default = dict)

    #company = models.CharField(max_length = 100, default = "")

    #organization = models.CharField(max_length = 100, default = "")

    def __unicode__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length = 100, default = "")
    conditions = JSONField(default = dict)
    feedback  = JSONField(default = dict)
    age = models.CharField(max_length = 100, default = "")
    email = models.CharField(max_length = 100, default = "")
    #company = models.CharField(max_length = 100, default = "")

    #organization = models.CharField(max_length = 100, default = "")

    def __unicode__(self):
        return self.name

class Initial(models.Model):
    name = models.CharField(max_length = 100, default = "")
    password = models.CharField(max_length = 100, default = "")
    email = models.CharField(max_length = 100, default = "")
    feedback = JSONField(default = dict)
    Doctor_list = JSONField(default = dict)
