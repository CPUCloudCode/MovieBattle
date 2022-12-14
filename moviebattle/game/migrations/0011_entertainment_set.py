# Generated by Django 3.2.7 on 2022-08-20 16:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_auto_20220801_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('plays', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('creator', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='')),
                ('title', models.CharField(default='', max_length=20)),
                ('poster', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('href', models.CharField(default='', max_length=200)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.set')),
            ],
        ),
    ]
