# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileManager',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('path', models.FileField(upload_to='files/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('sex', models.CharField(default='', blank=True, max_length=1, choices=[('F', 'female'), ('M', 'Male'), ('', '=======')])),
                ('image', models.ImageField(default='', upload_to='users/%Y/%m/%d', null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='filemanager',
            name='owner',
            field=models.ForeignKey(to='demo.UserProfile'),
        ),
    ]
