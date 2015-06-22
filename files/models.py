from django.db import models
from django.conf import settings
import os.path


class Release(models.Model):
    version = models.CharField(max_length=50, unique=True)
    version_num = models.IntegerField(default=0, unique=True)
    release_notes = models.TextField()
    featured = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)

    class Meta(object):
        ordering = ['version_num']

    def __unicode__(self):
        return self.version

    def save(self, *args, **kwargs):
        parts = [int(x) for x in self.version.split('.')]
        if len(parts) == 3:
            parts.append(0)
        assert len(parts) == 4
        self.version_num = (
            1000000 * parts[0] +
            10000 * parts[1] +
            100 * parts[2] +
            parts[3]
        )
        super(Release, self).save(*args, **kwargs)


class Download(models.Model):
    release = models.ForeignKey(Release)
    filename = models.CharField(max_length=50)
    size = models.IntegerField(default=0)
    md5 = models.CharField(max_length=32)
    sha1 = models.CharField(max_length=40)
    signed = models.BooleanField(default=False)

    class Meta(object):
        ordering = ['filename']
        unique_together = ['release', 'filename']

    def __unicode__(self):
        return '/phpMyAdmin/{0}/{1}'.format(
            self.release.version,
            self.filename
        )

    def get_absolute_url(self):
        return self.__unicode__()


class Theme(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    filename = models.CharField(max_length=200, unique=True)
    supported_versions = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=200)
    size = models.IntegerField(default=0)

    class Meta(object):
        ordering = ['name', 'version']

    def __unicode__(self):
        return u'{0} {1}'.format(self.name, self.version)
