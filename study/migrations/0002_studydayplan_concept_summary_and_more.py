# Generated by Django 5.2.3 on 2025-07-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studydayplan',
            name='concept_summary',
            field=models.TextField(blank=True, verbose_name='개념 요약'),
        ),
        migrations.AddField(
            model_name='studydayplan',
            name='prompt_example',
            field=models.TextField(blank=True, verbose_name='GPT 프롬프트 예시'),
        ),
        migrations.AddField(
            model_name='studyplan',
            name='plan_type',
            field=models.CharField(choices=[('summary', '요약 및 정리'), ('schedule', '스터디 플랜'), ('method', '공부법 추천'), ('qa', '질문/답변')], default='summary', max_length=50, verbose_name='활용 목적'),
        ),
    ]
