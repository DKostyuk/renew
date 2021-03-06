# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-12 20:32
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
            name='LogoImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='logo_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'LogoPhoto',
                'verbose_name_plural': 'LogoPhotos',
            },
        ),
        migrations.CreateModel(
            name='SliderMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_name', models.CharField(max_length=64)),
                ('ad_customer', models.CharField(max_length=64)),
                ('ad_description', models.TextField(blank=True, default=None, null=True)),
                ('ad_title', models.CharField(max_length=128)),
                ('ad_text', models.TextField(blank=True, default=None, null=True)),
                ('image', models.ImageField(upload_to='advert_images/')),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('position', models.IntegerField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('activation_date', models.DateField(blank=True, default=None)),
                ('deactivation_date', models.DateField(blank=True, default=None)),
            ],
            options={
                'verbose_name': 'SliderMain',
                'verbose_name_plural': 'SliderMains',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('email_confirm', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(blank=True, default=None, max_length=56, null=True)),
                ('index', models.CharField(blank=True, default=None, max_length=6, null=True)),
                ('street', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('locality', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('tel_number', models.CharField(blank=True, default=None, max_length=11, null=True)),
                ('company_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('nip', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('company_confirm', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MySubscriber',
                'verbose_name_plural': 'A lot of Subscribers',
            },
        ),
    ]
