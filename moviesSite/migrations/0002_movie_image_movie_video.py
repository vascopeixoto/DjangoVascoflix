# Generated by Django 4.2.13 on 2024-06-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesSite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
