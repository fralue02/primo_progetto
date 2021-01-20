from django.db import models
from django.urls import reverse

# Create your models here.
class Genere_lf(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome 
    
    class Meta:
        verbose_name="genere"
        verbose_name_plural="generi"

class Autore_lf(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome+" "+self.cognome 

    def get_absolute_url(self):

        return reverse("profilo_autore",kwargs={"pk":self.pk})


    class Meta:
        verbose_name="autore"
        verbose_name_plural="autori"

class Libro_lf(models.Model):  
    titolo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    autore = models.ForeignKey(Autore_lf, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Genere_lf)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name="libro"
        verbose_name_plural="libri"       
             

