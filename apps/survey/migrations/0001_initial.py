# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2021-04-24 13:23
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('answers', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
