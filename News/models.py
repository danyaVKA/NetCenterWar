from django.db import models

class Articales(models.Model):
    NAME_NEWS = models.CharField('NAME_NEWS', max_length=30)
    DATA_SOURCE = models.CharField('DATA_SOURCE', max_length=30)
    NEWS = models.TextField('NEWS')
    DATE = models.DateTimeField('DATE')

    def __str__(self):
        return self.NAME_NEWS

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
