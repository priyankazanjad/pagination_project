from django.db import models

class Student(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    publish_date = models.DateTimeField()
