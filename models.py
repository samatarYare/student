from django.db import models

class Student(models.Model):
    GENDER_CHOICES=[
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
    ]
    
    studentid = models.IntegerField()
    studentname= models.CharField(max_length=100)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    classes = models.CharField(max_length=100)
    
    def __str__(self):
        return self.studentname
    
    
