# Generated by Django 3.1.6 on 2021-02-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_slider_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='URL',
            field=models.URLField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='slider',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
