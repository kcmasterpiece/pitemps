# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tempGraph', '0004_auto_20150515_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readings',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
