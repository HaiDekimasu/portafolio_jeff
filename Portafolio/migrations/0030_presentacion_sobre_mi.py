# Generated by Django 3.2.6 on 2023-12-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0029_alter_presentacion_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentacion',
            name='sobre_mi',
            field=models.CharField(default=str, max_length=500),
            preserve_default=False,
        ),
    ]