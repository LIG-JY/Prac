from djongo import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class CommissionedArea(models.Model):
    city = models.CharField(null=True, default='', max_length=50)
    county = models.CharField(null=True, default='', max_length=50)
    emd = models.CharField(null=True, default='', max_length=50)
    con = models.CharField(null=True, default='', max_length=50)
    cop = models.CharField(null=True, default='', max_length=50)
    cot = PhoneNumberField(null=True, blank=False, unique=True)
    eon = models.CharField(null=True, default='', max_length=50)
    eop = models.CharField(null=True, default='', max_length=50)
    eot = PhoneNumberField(null=True, blank=False, unique=True)
    ln = models.CharField(null=True, default='', max_length=50)
    lt = PhoneNumberField(null=True, blank=False, unique=True)
