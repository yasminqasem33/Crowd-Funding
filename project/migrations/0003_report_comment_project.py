# Generated by Django 2.1 on 2019-04-26 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20190424_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_comment',
            name='project',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
            preserve_default=False,
        ),
    ]
