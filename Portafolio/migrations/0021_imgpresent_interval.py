# Generated by Django 3.2.6 on 2023-11-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0020_remove_imgpresent_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgpresent',
            name='interval',
            field=models.IntegerField(default=0),
        ),
    ]
