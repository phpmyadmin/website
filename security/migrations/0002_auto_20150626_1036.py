# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmasa',
            name='severity',
            field=models.TextField(),
        ),
    ]
