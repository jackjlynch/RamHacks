# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('languageName', models.TextField()),
                ('spaces', models.BooleanField(default=True)),
                ('wordList', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
