# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('course', models.IntegerField(null=True, blank=True)),
                ('group', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('department', models.ForeignKey(to='myapp.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('department', models.ForeignKey(to='myapp.Department')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='tutor',
            field=models.ForeignKey(to='myapp.Tutor'),
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(to='myapp.Faculty'),
        ),
        migrations.AddField(
            model_name='subject',
            name='department',
            field=models.ForeignKey(default=1, to='myapp.Department'),
            preserve_default=False,
        ),
    ]
