# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharpeapp', '0003_auto_20150831_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharpe',
            name='benchmark',
            field=models.CharField(default=b'SPY', max_length=4, choices=[(b'SPY', b'SPDR S&P 500 ETF (SPY)'), (b'VOO', b'Vanguard S&P 500 ETF (VOO)'), (b'IVV', b'iShares Core S&P 500 (IVV)')]),
        ),
    ]
