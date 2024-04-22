# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cpe_Due_Today(models.Model):

    #__Cpe_Due_Today_FIELDS__
    customer_number = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    #__Cpe_Due_Today_FIELDS__END

    class Meta:
        verbose_name        = _("Cpe_Due_Today")
        verbose_name_plural = _("Cpe_Due_Today")


class Find_Allowable_Equal_To_Billed(models.Model):

    #__Find_Allowable_Equal_To_Billed_FIELDS__
    cpt_code = models.CharField(max_length=255, null=True, blank=True)
    insurance_code = models.CharField(max_length=255, null=True, blank=True)

    #__Find_Allowable_Equal_To_Billed_FIELDS__END

    class Meta:
        verbose_name        = _("Find_Allowable_Equal_To_Billed")
        verbose_name_plural = _("Find_Allowable_Equal_To_Billed")



#__MODELS__END
