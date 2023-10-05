from django.db import models
# Create your models here.

class Yonalish(models.Model):
    nom = models.CharField(max_length=30)
    aktiv = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom = models.CharField(max_length=20)
    yonalish = models.ForeignKey(Yonalish,on_delete=models.CASCADE)
    asosiy = models.BooleanField()

    def __str__(self):
        return self.nom

j = (
    ("erkak","erkak"),
    ("ayol","ayol")
)

d = (
    ("Bakalavr","Bakalavr"),
    ("Magistr","Magistr")
)
class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=20,choices=j)
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=20,choices=d)
    fan = models.ForeignKey(Fan,on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

