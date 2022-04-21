from django.db import models

# Create your models here.
class Lecture(models.Model):
    title = models.CharField(max_length=200)
    room = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.pk}: {self:titls}'

class Student(models.Model):
    name = models.CharField(max_length=10)
    major = models.CharField(max_length=10)

    lectures = models.ManyToManyField(Lecture, related_name='students')

    def __str__(self):
        return f'{self.pk}: {self:name}'
