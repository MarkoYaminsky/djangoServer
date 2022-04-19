from django.db import models
from django_extensions.db.fields import SlugField
from django.utils.text import slugify


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField()
    slug = SlugField(unique=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.slug = '_'.join([slugify(self.first_name), slugify(self.last_name), slugify(self.id)])
        super(Student, self).save(*args, **kwargs)
