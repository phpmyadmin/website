# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-08-10 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0007_auto_20200505_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmasa',
            name='year',
            field=models.IntegerField(choices=[(2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2023),
        ),
    ]
