from django.db import models

class Userreg(models.Model):
    uname=models.CharField(max_length=100)
    usurname=models.CharField(max_length=100)
    uemail=models.CharField(max_length=100)
    uphone=models.CharField(max_length=100)
    class Meta:
        db_table="NewUserReg"