# Generated by Django 3.0.3 on 2020-03-09 13:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('software', '0002_exam_students'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='allotment',
            unique_together={('fid', 'date', 'sname')},
        ),
    ]