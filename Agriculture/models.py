from django.db import models


class Machinery(models.Model):
    partner_name = models.CharField(max_length=122, null=True)
    machinery = models.CharField(max_length=122, null=True)
    date = models.DateField(null=True)
    rent = models.IntegerField(null=True)

class Seeds(models.Model):
    partner_name = models.CharField(max_length=122, null=True)
    seeds = models.CharField(max_length=122, null=True)
    date = models.DateField(null=True)
    amount = models.IntegerField(null=True)


class Crops(models.Model):
    partner_name = models.CharField(max_length=122, null=True)
    crops = models.CharField(max_length=122, null=True)
    date = models.DateField(null=True)
    amt_bags = models.IntegerField(null=True)


class Purchase_Crops(models.Model):
    crop_name = models.CharField(max_length=122, null=True)
    date = models.DateField(null=True)
    amount_bags = models.IntegerField(null=True)
    price_crops = models.IntegerField(null=True)


class Loan(models.Model):
    loan_req = models.IntegerField(null=True)
    loan_returned = models.IntegerField(null=True)
    date = models.DateField(null=True)
    status = models.BooleanField(null=True,default=False)