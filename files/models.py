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
        ordering = ['-version_num']

    def __unicode__(self):
        return self.version

    def parse_version(self):
        if '-' in self.version:
            version, suffix = self.version.split('-')
            if suffix.startswith('alpha'):
                suffix_num = int(suffix[5:])
            elif suffix.startswith('beta'):
                suffix_num = 10 + int(suffix[4:])
            elif suffix.startswith('rc'):
                suffix_num = 50 + int(suffix[2:])
            else:
                raise ValueError(self.version)
        else:
            suffix_num = 99
            version = self.version
        parts = [int(x) for x in version.split('.')]
        if len(parts) == 3:
            parts.append(0)
        assert len(parts) == 4
        return (
            100000000 * parts[0] +
            1000000 * parts[1] +
            10000 * parts[2] +
            100 * parts[3] +
            suffix_num
        )

    def save(self, *args, **kwargs):
        self.version_num = self.parse_version()
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
