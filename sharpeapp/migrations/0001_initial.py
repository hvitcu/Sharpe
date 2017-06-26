# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sharpe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticker', models.CharField(max_length=4)),
                ('period', models.IntegerField(default=252)),
                ('sharpe', models.DecimalField(default=1, max_digits=9, decimal_places=4)),
            ],
        ),
    ]
