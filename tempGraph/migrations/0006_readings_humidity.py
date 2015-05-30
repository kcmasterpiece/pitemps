# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tempGraph', '0005_auto_20150515_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='readings',
            name='humidity',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=5),
        ),
    ]
