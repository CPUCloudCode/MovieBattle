# Generated by Django 3.2.7 on 2022-09-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_details_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='details',
            name='social',
            field=models.CharField(default='', max_length=200),
        ),
    ]