from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True, default=1)
    email = models.EmailField()
    course = models.CharField(max_length=100, default=" ")
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name