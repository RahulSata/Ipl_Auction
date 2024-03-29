# Generated by Django 2.0.2 on 2019-06-15 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_cur_players', models.IntegerField(default=0)),
                ('team_ruppe', models.FloatField(default=100)),
                ('team_logo', models.ImageField(upload_to='static/images/')),
                ('team_ihfew', models.CharField(max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=30)),
                ('player_team', models.CharField(default=False, max_length=30, null=True)),
                ('player_basePrice', models.FloatField(null=True)),
                ('player_soldprice', models.FloatField(default=None, null=True)),
                ('player_logo', models.ImageField(null=True, upload_to='static/images/players')),
                ('player_status', models.CharField(default=False, max_length=10)),
                ('player_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
