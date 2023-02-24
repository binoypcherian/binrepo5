from django.db import models

# Create your models here.
class Department(models.Model):
    dname = models.CharField(max_length=30)

    def __str__(self):
        return self.dname


class Course(models.Model):
    deptid = models.ForeignKey(Department, on_delete=models.CASCADE)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname


class Request(models.Model):
    rname = models.CharField(max_length=100,blank=False,null=False)
    rdob = models.DateField()
    rdept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    rcourse = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    Male='Male'
    FeMale='Female'
    Enquiry='Enquiry'
    Order='Order'
    Return='Return'
    Nill=0
    Paper=1
    Pen=2
    Text=3
    Note=4
    GENDER_CHOICE=((Male,'Male'),(FeMale,'Female'))
    PURPOSE_CHOICE=((Enquiry,'Enquiry'),(Order,'Order'),(Return,'Return'))

    gender=models.CharField(max_length=10,blank=False,null=False,choices=GENDER_CHOICE,default=Male)
    phone=models.CharField(max_length=10,blank=False,null=False)
    email=models.EmailField(max_length=50,blank=False,null=False)
    address=models.CharField(max_length=100,blank=False,null=False)
    purpose=models.CharField(max_length=50,blank=False,null=False,choices=PURPOSE_CHOICE)
    materials=models.CharField(max_length=50,null=False,default=Nill)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rname