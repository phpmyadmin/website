# Generated by Django 3.2.19 on 2023-08-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20200505_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='release',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]