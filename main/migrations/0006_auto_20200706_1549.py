# Generated by Django 2.2.1 on 2020-07-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200702_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
