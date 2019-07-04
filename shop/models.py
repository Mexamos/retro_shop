from django.db import models

class Offers(models.Model):
    name = models.CharField(null=True, blank=True,max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to="gallery", verbose_name='Изображение')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-name']