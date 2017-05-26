# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-25 12:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GForms', '0006_auto_20170525_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='question_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='Question')),
                ('answer_type', models.IntegerField(verbose_name='Answer Type')),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GForms.Forms')),
                ('form_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]