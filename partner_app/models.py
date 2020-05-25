from django.db import models

# Create your models here.
class PartnerInfo(models.Model):
    name_partner = models.CharField(max_length=100, blank=False, null=False, default='default'  )
    img = models.ImageField(upload_to='images/',max_length=150, blank=True, null=True)
    url = models.URLField( max_length=128, db_index=True, unique=True, blank=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_partner


class PartnerDescription(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
