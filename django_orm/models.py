from django.db import models

# Create your models here.

class Student(models.Model):
    stuName = models.CharField("Student name", max_length=70)
    stuAge = models.IntegerField('Student Age')
    stuEmail = models.EmailField('Student Email', max_length=70)
    stuMarks = models.IntegerField('Marks')

    def __str__(self):
        return self.stuName