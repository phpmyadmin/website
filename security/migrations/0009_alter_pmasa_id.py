# Generated by Django 3.2.19 on 2023-08-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0008_auto_20230810_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmasa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
