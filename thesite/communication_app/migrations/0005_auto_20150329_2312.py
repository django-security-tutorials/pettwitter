# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication_app', '0004_update_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.CharField(default=b'', max_length=1024, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='update',
            name='text',
            field=models.CharField(max_length=140),
            preserve_default=True,
        ),
    ]
