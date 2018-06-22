# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 05:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('firstname', models.CharField(blank=True, max_length=120, null=True)),
                ('lastname', models.CharField(blank=True, max_length=120, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('file', models.ImageField(blank=True, upload_to=b'profile_image')),
                ('image', models.ImageField(blank=True, upload_to=b'card_image')),
                ('birthday', models.DateField()),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('sname', models.CharField(blank=True, max_length=300, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=120)),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('phonenumber', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(max_length=120)),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('sname', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
