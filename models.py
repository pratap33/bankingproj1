from django.db import models
class user1(models.Model):
    uname=models.CharField(max_length=20,primary_key=True)
    pwrd=models.IntegerField()
    actbal=models.IntegerField(default=10000)
    splitbal=models.IntegerField(default=0000)
    paidto=models.CharField(max_length=20,default='None')
    facnum=models.IntegerField(default=0000)


