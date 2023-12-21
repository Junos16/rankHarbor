from django.db import models

class Student(models.Model):
    rank = models.IntegerField()
    quota = models.CharField(max_length = 5)
    seatType = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 20)
    year = models.IntegerField()
    roundNo = models.IntegerField()