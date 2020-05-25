from django.db import models

# Create your models here.
class Privacy(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False,  default='default')
    content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Privacys Inhalt"
        verbose_name = "Privacy Inhalt"

    def __str__(self):
        return self.title
