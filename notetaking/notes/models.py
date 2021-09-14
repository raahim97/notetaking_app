from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.user.email

# class Teacher(models.Model):
#     teacher = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100, null=True, blank=True)
#     last_name = models.CharField(max_length=100, null=True, blank=True)
#     email = models.CharField(max_length=100, null=True, blank=True)
#     phone_number = models.CharField(max_length=100, null=True, blank=True)
#     date_created = models.DateTimeField(auto_now=True, null=True, blank=True)
#
#     def __str__(self):
#         return self.user.email

class Note(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    note_desc = models.CharField(max_length=500, null=True, blank=True)
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return self.note_title