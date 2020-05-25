from django.db import models

# Create your models here.
class Join(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # nachricht_verschickt = models.BooleanField(default=False) هي مشان اذا بدي حدد انو انبعتلو رسالة ولا لأ وباقي الرسالة بلاقيها بالأدمن سايت

    class Meta:
        verbose_name_plural = "Newsletter"
        verbose_name = "Newsletter Abonierte"

    def __str__(self):
        return str(self.email)


class BeschreibungenHomeSeite(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    img = models.ImageField(upload_to='images/',max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_full = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('id', )
        verbose_name_plural = "Beschreibungen Homeseite"
        verbose_name = "Beschreibung Homeseite"
    def __str__(self):
        return self.title


class Vision(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Unser Vision"
        verbose_name = "Vision"

    def __str__(self):
        return self.title

class TreeathlonInZahlen(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    spenden_number = models.IntegerField()

    class Meta:
        verbose_name_plural = "Treeathlon in Zahlen Beschreibung"
        verbose_name = "TreeathlonInZahlen"

    def __str__(self):
        return self.title

class BackgroundImgDescription(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    title2 = models.CharField(max_length=100, blank=False, null=False, default = 'default')
    title3 = models.CharField(max_length=100, blank=False, null=False, default = 'default')
    content = models.TextField(blank=True, null=True)
    content2 = models.TextField(blank=True, null=True)
    content3 = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title
