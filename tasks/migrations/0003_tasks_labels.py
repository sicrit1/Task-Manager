# Generated by Django 4.1.3 on 2022-12-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_tasks_delete_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(to='labels.labels', verbose_name='label'),
        ),
    ]
