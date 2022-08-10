# Generated by Django 3.2.7 on 2022-06-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20220620_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='c1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='game',
            name='c2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='game',
            name='vote',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.CharField(default='', max_length=200),
        ),
    ]
