# Generated by Django 2.1.3 on 2021-06-13 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_auto_20210508_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='album',
            name='canciones',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='canciones',
        ),
        migrations.RemoveField(
            model_name='cancion',
            name='album_cancion',
        ),
        migrations.RemoveField(
            model_name='cancion',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='episodio',
            name='podcast_episodio',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='album_cancion_playlist',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='cancion_playlist',
        ),
        migrations.RemoveField(
            model_name='podcast',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='podcast',
            name='episodios',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='playlists_usuario',
        ),
        migrations.DeleteModel(
            name='album',
        ),
        migrations.DeleteModel(
            name='artista',
        ),
        migrations.DeleteModel(
            name='cancion',
        ),
        migrations.DeleteModel(
            name='episodio',
        ),
        migrations.DeleteModel(
            name='playlist',
        ),
        migrations.DeleteModel(
            name='podcast',
        ),
        migrations.DeleteModel(
            name='usuarios',
        ),
    ]
