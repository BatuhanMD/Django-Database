from django.db import models
from django.core.validators import MaxValueValidator,MinLengthValidator
# Create your models here.

class Fighter(models.Model):
    name  = models.CharField(max_length=60)
    age = models.IntegerField(validators=[MinLengthValidator(0),MaxValueValidator(100)])
    branch = models.CharField(max_length=50)
    win_score = models.IntegerField(default=0,validators=[MinLengthValidator(0)]) # Veritabanına sonradan eklendiği için default=0 veya null=True yapılması lazım
    draw_score = models.IntegerField(default=0,validators=[MinLengthValidator(0)]) # Veritabanına sonradan eklendiği için default=0 veya null=True yapılması lazım
    lose_score = models.IntegerField(default=0,validators=[MinLengthValidator(0)]) # Veritabanına sonradan eklendiği için default=0 veya null=True yapılması lazımpy

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Branch: {self.branch}, Win: {self.win_score}, Draw: {self.draw_score}, Lose: {self.lose_score}"