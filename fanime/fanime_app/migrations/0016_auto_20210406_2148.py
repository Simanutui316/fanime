# Generated by Django 3.1.7 on 2021-04-06 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fanime_app', '0015_auto_20210406_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fav_list',
            new_name='favs',
        ),
    ]
