# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extractore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('bank_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(unique=True, max_length=200)),
                ('password', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('useremailid', models.CharField(max_length=200)),
                ('email_from', models.CharField(max_length=200)),
                ('email_to', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('subject', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=200)),
                ('filedata', models.TextField()),
            ],
        ),
    ]
