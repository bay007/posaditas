# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=250)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('horario', models.TimeField()),
                ('tematica', models.CharField(max_length=250)),
                ('email_contacto', models.EmailField(max_length=254)),
                ('imagen_posada', models.URLField()),
            ],
        ),
    ]