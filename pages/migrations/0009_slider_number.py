# Generated by Django 3.1.6 on 2021-02-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20210217_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='number',
            field=models.CharField(default='5', max_length=2),
        ),
    ]
