from django.db import models
import datetime
from django.contrib.auth.models import User

class Register(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=122)
    name=models.CharField('Name',max_length=122)
    email=models.CharField('Email',max_length=122)
    pno=models.CharField('Phone Number',max_length=12)
    sclass=models.CharField(max_length=12,db_column='class')
    year=models.CharField('Year',max_length=12)
    passw=models.CharField(max_length=12)
    c_pass=models.CharField(max_length=12)
    date=models.DateField()

class Job_det(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    job_post=models.CharField(max_length=122)
    company_name=models.CharField(max_length=122)
    Company_email=models.CharField('Email',max_length=122)
    vacancy=models.IntegerField()
    salary=models.CharField(max_length=122)  
    location=models.CharField(max_length=122)
    last_date_toapply=models.DateField(max_length=122)
    
class Apply_for_job(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
   
    name=models.CharField('Name',max_length=122)
    email=models.CharField('Email',max_length=122)
    sclass=models.CharField(max_length=12)
    year=models.CharField('Year',max_length=12)
    company_name=models.CharField(max_length=122)
    class10clgname=models.CharField(max_length=122)
    class10per=models.CharField(max_length=122)
    class12clgname=models.CharField(max_length=122)
    class12per=models.CharField(max_length=122)
    job_post=models.CharField(max_length=122)
    status=models.CharField(max_length=122,null=True)
    resume=models.FileField(upload_to="image_resumes/")
    date = models.DateField(default=datetime.date.today)
    
    
class ShortlistedCand(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=122)
    name=models.CharField('Name',max_length=122)
    email=models.CharField('Email',max_length=122)
    sclass=models.CharField(max_length=12)
    year=models.CharField('Year',max_length=12)
    company_name=models.CharField(max_length=122)
    class10clgname=models.CharField(max_length=122)
    class10per=models.CharField(max_length=122)
    class12clgname=models.CharField(max_length=122)
    class12per=models.CharField(max_length=122)
    job_post=models.CharField(max_length=122)
    status=models.CharField(max_length=122,null=True)
    resume=models.FileField(upload_to="image_resumes/")
    