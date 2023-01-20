from django.db import models
from django.urls import reverse


class Data(models.Model):
    user = models.CharField(max_length=255)
    ip = models.CharField(max_length=100)
    data = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Данные'
        verbose_name_plural='Данные' 

    def __str__(self):
        return f"{self.user}'s data"

    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'pk': self.pk})
