# Generated by Django 4.2.2 on 2023-06-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='reviews/covers', verbose_name='cover'),
        ),
    ]
