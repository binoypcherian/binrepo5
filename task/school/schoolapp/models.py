from django.db import models
# Create your models here.

class Dep(models.Model):
    named = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return self.named

class Course(models.Model):
    department=models.ForeignKey(Dep,on_delete=models.CASCADE)
    namec=models.CharField(max_length=20)
    def __str__(self):
        return self.namec

class Req(models.Model):
    Male='Male'
    FeMale='Female'
    Enquiry='Enquiry'
    Order='Order'
    Return='Return'
    Paper='Paper'
    Pen='Pen'
    Text='Text'
    Note='Note'
    GENDER_CHOICE=((Male,'Male'),(FeMale,'Female'))
    PURPOSE_CHOICE=((Enquiry,'Enquiry'),(Order,'Order'),(Return,'Return'))
    MATERIAL_CHOICE=((Paper,'Paper'),(Pen,'Pen'),(Text,'Text Book'),(Note,'Note Book'))
    name=models.CharField(max_length=50,blank=False,null=False)
    dob=models.DateField()
    gender=models.CharField(max_length=10,blank=False,null=False,choices=GENDER_CHOICE,default=Male)
    phone=models.CharField(max_length=10,blank=False,null=False)
    email=models.EmailField(max_length=50,blank=False,null=False)
    address=models.CharField(max_length=100,blank=False,null=False)
    department = models.ForeignKey(Dep,on_delete=models.SET)
    course=models.ForeignKey(Course,on_delete=models.SET)
    purpose=models.CharField(max_length=50,blank=False,null=False,choices=PURPOSE_CHOICE)
    materials=models.TextField(blank=True,null=True,choices=MATERIAL_CHOICE)
    time=models.DateTimeField(auto_now_add=True)
