from django.db import models

class Batch(models.Model):
    batch_year = models.CharField(primary_key=True,max_length=4)
    
    def __str__(self):
        return (self.batch_year)
class Student(models.Model):
    batch_year=models.ForeignKey(Batch,on_delete=models.CASCADE)
    student_name = models.CharField('Student name',max_length=30,null=True)
    roll_num = models.CharField('Roll number',max_length=12,null=True)
    email = models.EmailField('Student email',primary_key=True,max_length=40)
    branch = models.CharField('Branch',null=True,max_length=20)

    def __str__(self):
        return (self.email)

class Company(models.Model):
    #batch_year = models.ForeignKey(Batch,on_delete=models.CASCADE)
    students=models.ManyToManyField(Student)
    company_name = models.CharField(primary_key=True,max_length=30)
    first_round = models.BooleanField(null=False,default=False)
    second_round = models.BooleanField(null = False,default=False)

    def __str__(self):
        return (self.company_name)
# Create your models here.
