from django.db import models
from django.utils import timezone
from django.utils.html import format_html
# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/',max_length=150, blank=True, null=True)
    content = models.TextField()
    link_text = models.CharField(max_length=50, default='facebook event')
    date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    url = models.URLField( max_length=128, db_index=True, unique=True, blank=True)


    class Meta:
        verbose_name_plural = "Unsere Events"
        verbose_name = "Event"

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.img:
            return format_html('<img src="{}" width="150" height="150" />'.format(self.img.url))
        else:
            return 'Hier ist noch kein Bild vorhanden'

    image_tag.short_description = 'Bild'
