# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication_app', '0003_auto_20150329_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='text',
            field=models.CharField(default='ignored', max_length=255),
            preserve_default=False,
        ),
    ]
