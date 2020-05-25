from django.db import models
from django.urls import reverse
# Create your models here.
class Teilnahme(models.Model):
    vorname   = models.CharField(max_length=100)
    nachname  = models.CharField(max_length=100)
    email     = models.EmailField(max_length=100)
    alter     = models.CharField(max_length=100)
    ergebnis_1  = models.CharField(max_length=100, blank=True, null=True)
    ergebnis_2  = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateTimeField("Erstellt am",auto_now_add=True, blank=True, null=True)


    class Meta:
        verbose_name_plural = "Teilnahmers"
        verbose_name = "TeilnehmerIn"


    def __str__(self):
        return self.vorname


    def get_absolute_url(self):
        return reverse('spenden_app:spenden_page')

# class Frage(models.Model):
#     frage = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.frage


class SpendeDescription(models.Model):
    title = models.CharField(max_length=70, blank=False, null=False,  default='default')
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
