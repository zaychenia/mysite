# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('kredits', models.FloatField(max_length=50)),
                ('semestr', models.CharField(max_length=50, null=True, blank=True)),
                ('group', models.IntegerField()),
                ('specialization', models.IntegerField(null=True, blank=True)),
                ('depends_on', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
