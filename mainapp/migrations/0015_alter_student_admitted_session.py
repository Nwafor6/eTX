# Generated by Django 4.1.3 on 2022-12-31 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_alter_department_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admitted_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.admittedsession'),
        ),
    ]
