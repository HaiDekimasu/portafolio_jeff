# Generated by Django 3.2.6 on 2023-12-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0028_alter_contacto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentacion',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]