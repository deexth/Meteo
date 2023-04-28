from django.db import models

# Create your models here.
class Weather(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Weather"
        verbose_name_plural = "Weathers"
    def __str__(self):
        return self.name