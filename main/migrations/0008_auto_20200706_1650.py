# Generated by Django 2.2.1 on 2020-07-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200706_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
