# Generated by Django 3.0.2 on 2020-01-18 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_topic_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='views',
        ),
    ]
