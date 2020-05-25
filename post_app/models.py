from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    kategorie = models.CharField(max_length=100, default='def')
    img = models.ImageField(upload_to='images/',max_length=150, blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    url = models.URLField( max_length=128, db_index=True, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Unser Blog"
        verbose_name = "Blog"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class SideWidget(models.Model):
    title = models.CharField(max_length=100, default='def')
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Side widgets (Weiß nicht auf Deutsch hahaha)"
        verbose_name = "Side widgets"

    def __str__(self):
        return self.title
