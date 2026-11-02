from django.db import models

class Redsocial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Red social")
    link = models.URLField(max_length=200, verbose_name="Enlace", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "red social"
        verbose_name_plural = "redes sociales"
        ordering = ['name']

    def __str__(self):
        return self.name
