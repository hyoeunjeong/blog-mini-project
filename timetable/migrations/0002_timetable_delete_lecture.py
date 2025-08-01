# Generated by Django 5.2.3 on 2025-07-03 16:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='과목명')),
                ('professor', models.CharField(blank=True, max_length=50, verbose_name='교수명')),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='강의실')),
                ('weekday', models.CharField(choices=[('MON', '월요일'), ('TUE', '화요일'), ('WED', '수요일'), ('THU', '목요일'), ('FRI', '금요일'), ('SAT', '토요일'), ('SUN', '일요일')], max_length=3, verbose_name='요일')),
                ('start_time', models.TimeField(verbose_name='시작 시간')),
                ('end_time', models.TimeField(verbose_name='종료 시간')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
    ]
