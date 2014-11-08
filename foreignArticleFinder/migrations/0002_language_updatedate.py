# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('foreignArticleFinder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='updateDate',
            field=models.DateTimeField(verbose_name='date last update', default=datetime.datetime(2014, 11, 8, 19, 39, 43, 866556, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
