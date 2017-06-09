# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-06-09 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0094_auto_20170608_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailystatisticsdepartment',
            name='current_activity_participants_age_avg',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsdepartment',
            name='current_activity_participants_age_max',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsdepartment',
            name='current_activity_participants_age_min',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsdepartment',
            name='volunteers_age_avg',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsdepartment',
            name='volunteers_age_max',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsdepartment',
            name='volunteers_age_min',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsregion',
            name='current_activity_participants_age_avg',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsregion',
            name='current_activity_participants_age_max',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsregion',
            name='current_activity_participants_age_min',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsregion',
            name='volunteers_age_avg',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsregion',
            name='volunteers_age_max',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsregion',
            name='volunteers_age_min',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsunion',
            name='current_activity_participants_age_avg',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsunion',
            name='current_activity_participants_age_max',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsunion',
            name='current_activity_participants_age_min',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsunion',
            name='volunteers_age_avg',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsunion',
            name='volunteers_age_max',
        ),
        migrations.RemoveField(
            model_name='dailystatisticsunion',
            name='volunteers_age_min',
        ),
        migrations.AddField(
            model_name='dailystatisticsgeneral',
            name='activity_participants_female',
            field=models.IntegerField(default=0, verbose_name='Deltagere på aktiviteter over al tid (piger)'),
        ),
        migrations.AddField(
            model_name='dailystatisticsgeneral',
            name='activity_participants_male',
            field=models.IntegerField(default=0, verbose_name='Deltagere på aktiviteter over al tid (drenge)'),
        ),
        migrations.AddField(
            model_name='dailystatisticsgeneral',
            name='payments',
            field=models.IntegerField(default=0, verbose_name='Betalinger sum'),
        ),
        migrations.AddField(
            model_name='dailystatisticsgeneral',
            name='payments_transactions',
            field=models.IntegerField(default=0, verbose_name='Betalinger transaktioner'),
        ),
        migrations.AddField(
            model_name='dailystatisticsgeneral',
            name='waitinglist_female',
            field=models.IntegerField(default=0, verbose_name='Piger på venteliste'),
        ),
        migrations.AddField(
            model_name='dailystatisticsgeneral',
            name='waitinglist_male',
            field=models.IntegerField(default=0, verbose_name='Drenge på venteliste'),
        ),
    ]
