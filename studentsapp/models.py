from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    subject = models.CharField(max_length=20)
    objects = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField()
    teachers = models.ManyToManyField(Teacher)
    objects = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name

