# Generated by Django 2.0.13 on 2019-04-29 11:20

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20190427_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=project.models.get_image_filename, verbose_name='Image'),
        ),
    ]
