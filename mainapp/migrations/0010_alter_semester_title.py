# Generated by Django 4.1.3 on 2022-11-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_remove_sessioncompleted_session_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
