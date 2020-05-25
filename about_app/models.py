from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False,  default='default')
    cover = models.ImageField(upload_to='images/',max_length=150, blank=True, null=True)
    our_description = models.TextField(blank=True, null=True)
    self_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Unser Team auf der About Seite"
        verbose_name = "Eine Person"

    def __str__(self):
        return self.name

class ContactInfo(models.Model):

    content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Unser Kontakt Info auf der Fusszeile unten"
        verbose_name = "content"

    def __str__(self):
        return self.content

class TeamDescription(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False,  default='default')
    content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Unser About Beschreibung auf der About Seite oben"
        verbose_name = "Contact Info"

    def __str__(self):
        return self.title
