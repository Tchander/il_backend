# Generated by Django 3.2.6 on 2021-09-03 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('international_league', '0013_auto_20210901_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='team_id',
        ),
        migrations.AddField(
            model_name='result',
            name='team',
            field=models.ForeignKey(default=4, help_text='Команда, к которой относится данный результат', on_delete=django.db.models.deletion.CASCADE, to='international_league.team', verbose_name='Team'),
            preserve_default=False,
        ),
    ]
