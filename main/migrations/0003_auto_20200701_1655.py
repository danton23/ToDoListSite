# Generated by Django 2.2.1 on 2020-07-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_todolist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
