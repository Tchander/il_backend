# Generated by Django 3.2.6 on 2021-08-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_league', '0004_pilot_number_of_races_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilot',
            name='position_in_the_last_qualifying',
            field=models.CharField(default='', help_text='Позиция в последней квалификации', max_length=20, verbose_name='Position in the last qualifying'),
        ),
        migrations.AddField(
            model_name='pilot',
            name='position_in_the_last_race',
            field=models.CharField(default='', help_text='Позиция в последней гонке', max_length=20, verbose_name='Position in the last race'),
        ),
        migrations.AlterField(
            model_name='result',
            name='qualifying_position',
            field=models.CharField(default='DNQ', help_text='Позиция в квалификации', max_length=20, verbose_name='Qualifying position'),
        ),
    ]
