# Generated by Django 3.1.2 on 2020-10-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='image_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='budget',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
