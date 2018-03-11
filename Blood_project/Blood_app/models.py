from django.db import models

# Create your models here.
# class Dhirajlal_gandhi_college_of_technology(models.Model):

class Add_donors(models.Model):
    student_name = models.CharField(max_length = 264,unique=True)
    batch = models.CharField(max_length = 10)
    address = models.CharField(max_length=264)
    blood_group= models.CharField(max_length=5)
    mobile_number = models.CharField(max_length=10,unique=True)
    date_of_birth =models.DateField()

    def __str__(self):
        return self.batch
