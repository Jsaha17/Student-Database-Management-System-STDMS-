# Generated by Django 5.1.6 on 2025-04-13 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_subject_studentprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='studentProfile',
        ),
    ]
