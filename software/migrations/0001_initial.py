# Generated by Django 3.0.3 on 2020-03-07 12:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildingname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('did', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField(default=0)),
                ('etimetable', models.FileField(default='e.txt', upload_to='ftimetable')),
                ('year', models.IntegerField(default=1)),
                ('allot', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='fdetail',
            fields=[
                ('fid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('countofduties', models.IntegerField(default=0)),
                ('timetable', models.FileField(upload_to='ftimetable')),
                ('did', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='software.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('scode', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomno', models.CharField(max_length=20)),
                ('roomtt', models.FileField(upload_to='ftimetable')),
                ('strength', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('Timestamp', models.DateTimeField()),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.fdetail')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.Department'),
        ),
        migrations.CreateModel(
            name='Availablerooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('Time', models.CharField(max_length=20)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.Rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('Time', models.CharField(max_length=20)),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='allotment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='1', max_length=20)),
                ('time', models.CharField(default='0', max_length=30)),
                ('ename', models.CharField(default='P0', max_length=20)),
                ('semester', models.CharField(default='S0', max_length=10)),
                ('sname', models.CharField(default='XYZ', max_length=30)),
                ('alter', models.BooleanField(default=False)),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('roomno', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='software.Rooms')),
            ],
        ),
        migrations.CreateModel(
            name='f_sem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=10)),
                ('fid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='software.fdetail')),
            ],
            options={
                'unique_together': {('fid',)},
            },
        ),
    ]
