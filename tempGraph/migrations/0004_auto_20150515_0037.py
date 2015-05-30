# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tempGraph', '0003_auto_20150515_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readings',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 15, 0, 37, 27, 509632, tzinfo=utc)),
        ),
    ]
