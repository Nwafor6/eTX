# Generated by Django 4.1.3 on 2022-12-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_alter_admittedsession_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
