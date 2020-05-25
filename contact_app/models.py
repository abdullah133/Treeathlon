from django.db import models

# Create your models here.
class ContactAdressen(models.Model):
    adresse = models.CharField(max_length=40, blank=False, null=False,  default='default')
    telefon = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Unser Kontakt info auf der Contact Seite"
        verbose_name = "Contact Info"

    def __str__(self):
        return self.adresse


class ContactUsInfo(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False,  default='default')
    content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Unser Kontakt Beschreibung auf der Contact Seite oben"
        verbose_name = "Beschreibung"

    def __str__(self):
        return self.title
