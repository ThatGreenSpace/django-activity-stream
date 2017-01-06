# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0002_remove_action_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='estate',
            field=models.PositiveSmallIntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
