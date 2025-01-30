from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    health_score = models.FloatField()
    
    def __str__(self):
        return self.name
