# Generated by Django 3.2.6 on 2023-11-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0022_remove_imgpresent_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgpresent',
            name='imagen',
            field=models.ImageField(upload_to='Portafolio/images/'),
        ),
    ]