from django.db import models


class Release(models.Model):
    version = models.CharField(max_length=50)
    release_notes = models.TextField()
    featured = models.BooleanField()
    visible = models.BooleanField()

    def __unicode__(self):
        self.relese.version


class Download(models.Model):
    release = models.ForeignKey(Release)
    filename = models.CharField(max_length=50)
    md5 = models.CharField(max_length=32)
    sha1 = models.CharField(max_length=40)
    signed = models.BooleanField(default=False)

    def __unicode__(self):
        return '/phpMyAdmin/{0}/{1}'.format(
            self.relese.version,
            self.filename
        )

    def get_absolute_url(self):
        return self.__unicode__()


# TODO: themes
