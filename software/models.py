from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date,time,datetime

# Create your models here.#rooms=models.ManyToOneRel(allotment,on_delete=models.CASCADE)

class Department(models.Model):
    did=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=30,null=False)

class fdetail(models.Model):
    fid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    countofduties = models.IntegerField(default=0)
    timetable = models.FileField(upload_to='ftimetable')
    did=models.ForeignKey(Department,on_delete=models.CASCADE,default=1)

class Exam(models.Model):
    eid=models.IntegerField(null=False,default=0)
    etimetable = models.FileField(upload_to='ftimetable',default="e.txt")
    year=models.IntegerField(null=False,default=1)
    allot=models.BooleanField(default=False)

class Subject(models.Model):
    scode=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=15)


class Strength(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    year=models.IntegerField(null=False)
    strength=models.IntegerField(null=False)

class Building(models.Model):
    buildingname=models.CharField(max_length=20)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
class Rooms(models.Model):
    roomno=models.CharField(max_length=20)
    building=models.ForeignKey(Building,on_delete=models.CASCADE)
class allotment(models.Model):
    fid=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.CharField(max_length=20,default="1")
    time=models.CharField(max_length=30,default="0")
    ename=models.CharField(max_length=20,default="P0")
    semester=models.CharField(max_length=10,default="S0")
    sname=models.CharField(max_length=30,default="XYZ")
    roomno=models.ForeignKey(Rooms,on_delete=models.CASCADE,default=0)
    alter=models.BooleanField(default=False)
class Available(models.Model):
    fid = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    Time = models.CharField(max_length=20)
class f_sem(models.Model):
    semester=models.CharField(max_length=10)
    fid = models.OneToOneField(fdetail, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("fid", ),)
class Notification(models.Model):
    fid=models.ForeignKey(fdetail,on_delete=models.CASCADE)
    date=models.DateTimeField()
    Timestamp=models.DateTimeField()