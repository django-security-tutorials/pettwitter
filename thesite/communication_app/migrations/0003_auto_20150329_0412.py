# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication_app', '0002_auto_20150329_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
