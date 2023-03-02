from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "students"

    def __str__(self):
        return self.firstname
