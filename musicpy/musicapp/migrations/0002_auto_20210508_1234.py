# Generated by Django 2.1.3 on 2021-05-08 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancion',
            old_name='albumes',
            new_name='album_cancion',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='podcasts',
            new_name='podcast_episodio',
        ),
        migrations.RenameField(
            model_name='playlist',
            old_name='album',
            new_name='album_cancion_playlist',
        ),
        migrations.RenameField(
            model_name='playlist',
            old_name='cancion',
            new_name='cancion_playlist',
        ),
        migrations.RenameField(
            model_name='usuarios',
            old_name='playlist',
            new_name='playlists_usuario',
        ),
    ]
