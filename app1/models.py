from django.db import models


class User(models.Model):
    id_no = models.IntegerField(primary_key=True, default=False)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)


class Plots(models.Model):
    regno = models.IntegerField(primary_key=True, default=False)
    plotno = models.IntegerField()
    roadno = models.IntegerField()
    surveyno = models.IntegerField()
    costpersqyard = models.IntegerField()
    otherexp = models.DecimalField(max_digits=10, decimal_places=2)
    boundary = models.IntegerField()
    facing = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    totalcost = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='plots/')


class Appartment(models.Model):
    regno = models.IntegerField(primary_key=True, default=False)
    appart_no = models.IntegerField()
    roadno = models.IntegerField()
    surveyno = models.IntegerField()
    costpersqyard = models.IntegerField()
    otherexp = models.DecimalField(max_digits=10, decimal_places=2)
    facing = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    totalcost = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='appartment/')


class Employee(models.Model):
    id_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    mailid = models.EmailField()
    location = models.CharField(max_length=30)
    doj = models.DateField()
    role = models.CharField(max_length=20)
    remarks = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='employee/')
