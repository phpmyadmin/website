from django.db import models
from django.conf import settings
import os.path
from data.themes import CSSMAP

# Naming of versions
VERSION_INFO = (
    ('beta1', ' First beta version.'),
    ('beta2', ' Second beta version.'),
    ('beta3', ' Third beta version.'),
    ('beta4', ' Fourth beta version.'),
    ('beta', ' Beta version.'),
    ('rc1', ' First release candidate.'),
    ('rc2', ' Second release candidate.'),
    ('rc3', ' Third release candidate.'),
    ('rc4', ' Fourth release candidate.'),
    ('rc', ' Release candidate.'),
)


class Release(models.Model):
    version = models.CharField(max_length=50, unique=True)
    version_num = models.IntegerField(default=0, unique=True)
    release_notes = models.TextField()
    stable = models.BooleanField(default=False, db_index=True)

    class Meta(object):
        ordering = ['-version_num']

    def __unicode__(self):
        return self.version

    def simpledownload(self):
        try:
            return self.download_set.get(
                filename__endswith='-all-languages.zip'
            )
        except Download.DoesNotExist:
            return self.download_set.all()[0]

    @staticmethod
    def parse_version(version):
        if '-' in version:
            version, suffix = version.split('-')
            if suffix.startswith('alpha'):
                suffix_num = int(suffix[5:])
            elif suffix.startswith('beta'):
                suffix_num = 10 + int(suffix[4:])
            elif suffix.startswith('rc'):
                suffix_num = 50 + int(suffix[2:])
            else:
                raise ValueError(version)
        else:
            suffix_num = 99
            version = version
        parts = [int(x) for x in version.split('.')]
        if len(parts) == 2:
            parts.append(0)
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
        self.version_num = self.parse_version(self.version)
        self.stable = self.version_num % 100 == 99
        super(Release, self).save(*args, **kwargs)

    def get_version_suffix(self):
        '''
        Returns suffix for a version.
        '''
        for match, result in VERSION_INFO:
            if self.version.find(match) != -1:
                return result
        return ''

    def get_version_info(self):
        '''
        Returns description to the phpMyAdmin version.
        '''
        if self.version[:2] == '1.':
            text = 'Historical release.'
        elif self.version[:2] == '2.':
            text = 'Version compatible with PHP 4+ and MySQL 3+.'
        elif self.version[:2] == '3.':
            text = (
                'Frames version not requiring Javascript. ' +
                'Requires PHP 5.2 and MySQL 5. ' +
                'Supported for security fixes only, until Jan 1, 2014.'
            )
        elif self.version[:3] == '4.4':
            text = 'Current version compatible with PHP 5.3 and MySQL 5.5.'
        elif self.version[:3] == '4.3':
            text = (
                'Older version compatible with PHP 5.3 and MySQL 5.5.' +
                'Supported for security fixes only, until Oct 1, 2015.'
            )
        elif self.version[:3] == '4.2':
            text = (
                'Older version compatible with PHP 5.3 and MySQL 5.5.' +
                'Supported for security fixes only, until Jul 1, 2015.'
            )
        elif self.version[:3] == '4.1':
            text = (
                'Older version compatible with PHP 5.3 and MySQL 5.5.' +
                'Supported for security fixes only, until Jan 1, 2015.'
            )
        elif self.version[:3] == '4.0':
            text = (
                'Older version compatible with PHP 5.2 and MySQL 5. ' +
                'Supported for security fixes only, until Jan 1, 2017.'
            )
        text += self.get_version_suffix()

        return text



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
        return 'https://files.phpmyadmin.net{0}'.format(
            self.__unicode__()
        )

    @property
    def archive(self):
        return self.filename.rsplit('.', 1)[-1]


class Theme(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    filename = models.CharField(max_length=200, unique=True)
    supported_versions = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=200)
    size = models.IntegerField(default=0)
    md5 = models.CharField(max_length=32)
    sha1 = models.CharField(max_length=40)
    signed = models.BooleanField(default=False)

    class Meta(object):
        ordering = ['name', 'version']

    def __unicode__(self):
        return u'{0} {1}'.format(self.display_name, self.version)

    @property
    def imgname(self):
        return 'images/themes/{0}.png'.format(self.name)

    def get_absolute_url(self):
        return 'https://files.phpmyadmin.net/themes/{0}/{1}/{2}'.format(
            self.name,
            self.version,
            self.filename,
        )

    @property
    def get_css(self):
        return CSSMAP[self.supported_versions]
