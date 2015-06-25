from django.db import models


class Translation(models.Model):
    url = models.URLField(unique=True)
    name = models.CharField(max_length=100)
    translated = models.IntegerField()
    percent = models.DecimalField(max_digits=4, decimal_places=1)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta(object):
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.url

    @property
    def css(self):
        if self.percent < 50:
            return ' b50'
        elif self.percent < 80:
            return ' b80'
        return ''
