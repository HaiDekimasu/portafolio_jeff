# Generated by Django 3.2.6 on 2023-11-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0018_alter_imgpresent_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgpresent',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
