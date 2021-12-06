# Generated by Django 3.2.6 on 2021-12-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_league', '0014_auto_20210903_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='race_table_position',
            field=models.PositiveSmallIntegerField(default=0, help_text='Позиция в гонке для таблицы', verbose_name='Race table position'),
        ),
        migrations.AddField(
            model_name='team',
            name='total_score_league3',
            field=models.DecimalField(decimal_places=1, default=0, help_text='Количество очков в кубке конструкторов лиги 3', max_digits=5, verbose_name='Total score league 3'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='league',
            field=models.PositiveSmallIntegerField(default=3, help_text='Номер лиги, в которой выступает пилот', verbose_name='League'),
        ),
        migrations.AlterField(
            model_name='team',
            name='total_score_league2',
            field=models.DecimalField(decimal_places=1, default=0, help_text='Количество очков в кубке конструкторов лиги 2', max_digits=5, verbose_name='Total score league 2'),
        ),
    ]