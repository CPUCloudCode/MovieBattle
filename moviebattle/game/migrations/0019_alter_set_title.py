# Generated by Django 3.2.7 on 2022-09-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0018_auto_20220925_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
