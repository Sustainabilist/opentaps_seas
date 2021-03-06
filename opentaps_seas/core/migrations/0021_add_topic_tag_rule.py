# This file is part of opentaps Smart Energy Applications Suite (SEAS).

# opentaps Smart Energy Applications Suite (SEAS) is free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# opentaps Smart Energy Applications Suite (SEAS) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with opentaps Smart Energy Applications Suite (SEAS).
# If not, see <https://www.gnu.org/licenses/>.


# Generated by Django 2.0.13 on 2019-05-06 14:08

from django.db import migrations, models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import HStoreField


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_add_timezones_geo_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicTagRule',
            fields=[
                ('rule_name', models.CharField(max_length=255, primary_key=True)),
                ('filters', ArrayField(HStoreField(blank=True, null=True))),
                ('tags', ArrayField(HStoreField(blank=True, null=True))),
            ],
        ),
    ]
