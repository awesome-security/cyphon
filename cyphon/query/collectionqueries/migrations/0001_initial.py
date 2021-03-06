# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.10.1 on 2017-03-20 16:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('warehouses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('joiner', models.CharField(choices=[('AND', 'AND'), ('OR', 'OR')], max_length=40)),
                ('collections', models.ManyToManyField(related_name='_collectionquery_collections_+', to='warehouses.Collection')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fieldset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=255)),
                ('field_type', models.CharField(choices=[('BooleanField', 'BooleanField'), ('CharField', 'CharField'), ('ChoiceField', 'ChoiceField'), ('DateTimeField', 'DateTimeField'), ('EmailField', 'EmailField'), ('FileField', 'FileField'), ('FloatField', 'FloatField'), ('IntegerField', 'IntegerField'), ('GenericIPAddressField', 'IPAddressField'), ('ListField', 'ListField'), ('PointField', 'PointField'), ('TextField', 'TextField'), ('URLField', 'URLField'), ('EmbeddedDocument', 'EmbeddedDocument')], max_length=255)),
                ('operator', models.CharField(choices=[('eq', 'equals'), ('in', 'contains'), ('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'), ('regex', 'contains'), ('not:eq', 'does not equal'), ('not:in', 'does not contain'), ('not:regex', 'does not contain'), ('not:missing', 'is not null'), ('within', 'within')], max_length=40)),
                ('value', models.TextField()),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fieldsets', related_query_name='fieldset', to='collectionqueries.CollectionQuery')),
            ],
        ),
    ]
