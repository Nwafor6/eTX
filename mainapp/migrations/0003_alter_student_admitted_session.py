# Generated by Django 4.1.3 on 2022-11-27 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_semester_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admitted_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.admittedsession'),
        ),
    ]
