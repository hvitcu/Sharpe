# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharpeapp', '0004_sharpe_benchmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharpe',
            name='tenYearNoteYield',
            field=models.FloatField(default=5.0),
        ),
    ]
