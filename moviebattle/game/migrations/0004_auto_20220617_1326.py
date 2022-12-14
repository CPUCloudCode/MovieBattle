# Generated by Django 3.2.7 on 2022-06-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_game_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='round',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='game',
            name='rounds',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='movie',
            name='href',
            field=models.CharField(default='https://media.istockphoto.com/vectors/movie-time-vector-illustration-cinema-poster-concept-on-red-round-vector-id911590226?k=20&m=911590226&s=612x612&w=0&h=HlJtSKF-fLsKFy1QJ-EVnxXkktBKNS-3jUQPXsSasYs=', max_length=200),
        ),
    ]
