# Generated by Django 3.2.6 on 2023-11-30 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0021_imgpresent_interval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgpresent',
            name='interval',
        ),
    ]
