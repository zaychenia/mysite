from django.db import models
from django.contrib.auth.models import AbstractUser, User

class Faculty(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)

    def __unicode__(self):
        return unicode(str(self.id).ljust(2, ' ')) + ' / ' + unicode(self.name)

class Department(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    faculty = models.ForeignKey(Faculty)

    def __unicode__(self):
        return unicode(str(self.id).ljust(2, ' ')) + ' / ' + unicode(self.name)

class Subject(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    kredits = models.FloatField(max_length=50)
    semestr = models.CharField(max_length=50, null=True, blank=True)
    group = models.IntegerField()
    specialization = models.IntegerField(null=True, blank=True)
    depends_on = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return unicode(str(self.id).ljust(2, ' ')) + ' / ' + unicode(self.name) + ' / Credits = ' + unicode(self.kredits) + \
               ' Semester = ' + unicode(self.semestr)

# class UserProfile(AbstractUser):
#     pass

class Tutor(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department)


class Student(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    course = models.IntegerField(null=True, blank=True)
    group = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department)
    tutor = models.ForeignKey(Tutor)

