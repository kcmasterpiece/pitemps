# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tempGraph', '0002_readings_temp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='readings',
            options={'get_latest_by': 'time'},
        ),
        migrations.AddField(
            model_name='readings',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
