# Generated by Django 3.1.7 on 2021-04-07 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fanime_app', '0016_auto_20210406_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanime_app.profile'),
        ),
    ]
