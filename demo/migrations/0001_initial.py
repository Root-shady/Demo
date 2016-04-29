# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileManager',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('path', models.FileField(upload_to='files/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('confirem_password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(max_length=1, blank=True, default='', choices=[('F', 'female'), ('M', 'Male'), ('', '=======')])),
                ('image', models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='filemanager',
            name='owner',
            field=models.ForeignKey(to='demo.UserProfile'),
        ),
    ]
