from django.db import models
from markupfield.fields import MarkupField
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(db_index=True, unique_for_date='date')
    date = models.DateTimeField(db_index=True)
    body = MarkupField(default_markup_type='markdown')
    author = models.ForeignKey(User)

    class Meta(object):
        ordering = ['-date']

    def __unicode__(self):
        return self.title
