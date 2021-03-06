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

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190506_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('geo_code_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Geo Code ID')),
                ('geo_code_type_id', models.CharField(max_length=255, verbose_name='Geo Code Type ID')),
                ('geo_code_name', models.CharField(max_length=255, verbose_name='Geo Code Name')),
                ('parent_geo_code_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
