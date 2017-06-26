# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharpeapp', '0005_sharpe_tenyearnoteyield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharpe',
            name='period',
        ),
        migrations.AddField(
            model_name='sharpe',
            name='trade_period',
            field=models.IntegerField(default=252),
        ),
    ]
