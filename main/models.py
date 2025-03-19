from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    guruh = models.CharField(max_length=20)
    kurs = models.IntegerField()
    kitob_soni = models.IntegerField(default=0)

    def __str__(self):
        return self.ism

class Muallif(models.Model):
    ism = models.CharField(max_length=100)
    jins = models.CharField(max_length=10, choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')])
    tugilgan_sana = models.DateField()
    kitob_soni = models.IntegerField(default=0)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=200)
    janr = models.CharField(max_length=50)
    sahifa = models.IntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Admin(models.Model):
    ism = models.CharField(max_length=100)
    ish_vaqti = models.CharField(max_length=50)

    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sana = models.DateField()

    def __str__(self):
        return f"{self.talaba} - {self.kitob}"

