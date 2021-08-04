from django.db import models

# Create your models here.

class Pet(models.Model):
    petId = models.CharField(max_length=32, unique=True)
    nome_pet = models.CharField(max_length=50)
    dono = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    nascimento = models.IntegerField()

    def __str__(self):
        return self.petId


class Picture(models.Model):
    petId = models.ForeignKey('Pet', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pets')

    def __str__(self):
        return str(self.petId)