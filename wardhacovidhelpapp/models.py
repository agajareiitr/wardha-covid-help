from django.db import models
from django.db.models.fields import BooleanField, CharField

from django.utils import timezone
# Create your models here.

class PlasmaRequest(models.Model):
    bloodgroupchoices = (("O+","O+"),("O-","O-"),("A+","A+"),("A-","A-"),("B+","B+"),("B-","B-"),("AB+","AB+"),("AB-","AB-"),("Dontknow","Dont know"),)
    Genderchoices = (("Male","Male"),("Female","Female"),("other","other"))

    Name = models.CharField(max_length=200,null=True)
    Age = models.CharField(max_length=2,null=True)
    Gender = models.CharField(max_length=50,choices=Genderchoices)
    BloodGroup =  models.CharField("Blood Group",max_length=50,choices=bloodgroupchoices)
    PhoneNumber = models.CharField("Phone Number",max_length=10,null=True)
    HospitalName = models.CharField("Hospital Name",max_length=500,null=True)
    DateOfPositive = models.DateField("Date of Positive (dd/mm/yyyy)",auto_now_add=False,auto_now=False)
    DateCreated = models.DateField("Date Created",auto_now_add=True,auto_now=False)
    verified = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        displayName = self.Name+" | "+self.Gender+" / "+str(self.Age)
        return displayName
    
    class Meta:
        ordering = ["complete"]

class PlasmaDonar(models.Model):
    bloodgroupchoices = (("O+","O+"),("O-","O-"),("A+","A+"),("A-","A-"),("B+","B+"),("B-","B-"),("AB+","AB+"),("AB-","AB-"),("Dontknow","Dont know"))
    Genderchoices = (("Male","Male"),("Female","Female"),("other","other"))

    Name = models.CharField(max_length=200,null=True)
    Age = models.CharField(max_length=2,null=True)
    Gender = models.CharField(max_length=50,choices=Genderchoices)
    BloodGroup =  models.CharField("Blood Group",max_length=50,choices=bloodgroupchoices)
    PhoneNumber = models.CharField("Phone Number",max_length=10,null=True)
    DateOfNegative = models.DateField("Date of Negative (dd/mm/yyyy)",auto_now_add=False,auto_now=False)
    DateCreated = models.DateField("Date Created",auto_now_add=True,auto_now=False)
    verified = models.BooleanField(default=False)


    def __str__(self):
        displayName = self.Name+" | "+self.Gender+" / "+str(self.Age)
        return displayName


    class Meta:
        ordering = ['-verified']


class TeamMembers(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Profession = models.CharField(max_length=200,null=True)
    Title = models.TextField(max_length=500,null=True)
    ProfileImage = models.ImageField(null=True,blank=True)
    JoiningDate = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Name



class HospitalData(models.Model):
    HospitalName = models.CharField(max_length=300,null=True)
    Address = models.TextField(max_length=300,null=True)
    PhoneNumber = models.CharField(max_length=50,null=True)
    Verified = BooleanField(default=False)

    def __str__(self):
        return f"{self.HospitalName}"
    
    class Meta:
        verbose_name_plural = "Hospital Data"

class CovidNewsPost(models.Model):
    Title = models.CharField(max_length=300,null=True)
    Short_Discription = models.TextField(null=True)
    News_Image = models.ImageField(upload_to = 'newsimages')
    Paragraph_1 = models.TextField(null=True,blank=True)
    Paragraph_2 = models.TextField(null=True,blank=True)
    Paragraph_3 = models.TextField(null=True,blank=True)
    Paragraph_4 = models.TextField(null=True,blank=True)
    Paragraph_5 = models.TextField(null=True,blank=True)
    Paragraph_6 = models.TextField(null=True,blank=True)
    Paragraph_7 = models.TextField(null=True,blank=True)
    Paragraph_8 = models.TextField(null=True,blank=True)
    Paragraph_9 = models.TextField(null=True,blank=True)
    Paragraph_10 = models.TextField(null=True,blank=True)
    

    Date_Created = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.Title


class VaccineAvailablity(models.Model):
    Name = models.CharField(max_length=200,null=True)
    AvailableCapacity = models.CharField(max_length=5,null=True)
    VaccineName = models.CharField(max_length=100,null=True)
    MinAgeLimit = models.CharField(max_length=3,null=True)
    BlockName = models.CharField(max_length=100,null=True)
    DistrictName = models.CharField(max_length=100,null=True)
    FeeType = models.CharField(max_length=100,null=True)
    LastUpdated = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name_plural = "Vaccine Availablity"

class Groceries(models.Model):
    Delivery_choices = (("Free Delivery","Free Delivery"),("Paid Delivery","Paid Delivery"))
    Store_Name = models.CharField(max_length=200,null=True)
    Address = models.TextField(max_length=300,null=True)
    Phone_Number = models.CharField(max_length=200,null=True)
    Delivery_Type = models.CharField(max_length=50,choices=Delivery_choices,null=True)
    Store_Remarks = models.TextField(max_length=500,null=True)
    Admin_Verified = models.BooleanField(default=False)

    def __str__(self):
        return self.Store_Name

    class Meta:
        verbose_name_plural = "Groceries"