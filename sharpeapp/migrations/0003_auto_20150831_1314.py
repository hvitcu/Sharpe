# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sharpeapp', '0002_remove_sharpe_sharpe'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharpe',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2015, 8, 31, 12, 14, 46, 670000, tzinfo=utc), verbose_name=b'End Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sharpe',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2015, 8, 31, 12, 14, 55, 798000, tzinfo=utc), verbose_name=b'Start Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sharpe',
            name='period',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='sharpe',
            name='ticker',
            field=models.CharField(help_text=b'Market Symbol', max_length=4),
        ),
    ]
