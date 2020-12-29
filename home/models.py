from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    decr = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name

class Recruitment(models.Model):
    sno=models.AutoField(primary_key=True)
    orgName=models.CharField(max_length=250)
    slug=models.CharField(max_length=100,default='')
    content=models.TextField()
    user=models.ManyToManyField(User )
    date=models.DateField()
    def __str__(self):
        return self.orgName
    
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=30,default='')
    lname=models.CharField(max_length=30,default='')
    roll = models.IntegerField( blank=True)
    address=models.TextField()
    branch=models.TextField()
    document=models.FileField(upload_to='resume',default='')
    def __str__(self):
        return self.fname

class Enrollment(models.Model):
    recruiter=models.ForeignKey(Recruitment,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_applied=models.DateField()

    class Meta:
        unique_together=[['user','recruiter']]

    

    
    
    
    

    