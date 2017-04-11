# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0003_action_estate'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='system_admin',
            field=models.BooleanField(db_index=True, default=False),
            preserve_default=True,
        ),
    ]
