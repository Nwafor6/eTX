# Generated by Django 4.1.3 on 2023-02-05 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_rename_session_title_cgpa_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cgpa',
            name='semester',
        ),
    ]
