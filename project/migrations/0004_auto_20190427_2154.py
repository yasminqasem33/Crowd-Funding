# Generated by Django 2.1 on 2019-04-27 21:54

from django.db import migrations, models
import django.db.models.deletion
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_report_comment_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=project.models.get_image_filename, verbose_name='Image')),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='picture',
            name='project',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
