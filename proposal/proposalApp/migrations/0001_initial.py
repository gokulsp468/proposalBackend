# Generated by Django 4.2.11 on 2024-04-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=255, verbose_name='Client ID')),
                ('project_name', models.CharField(max_length=255, verbose_name='Project Name')),
                ('project_type', models.CharField(blank=True, max_length=100, verbose_name='Project Type')),
                ('platform', models.CharField(blank=True, max_length=100, verbose_name='Platform')),
                ('other_platform', models.CharField(blank=True, max_length=100, verbose_name='Other Platform')),
                ('template_id', models.CharField(max_length=255, verbose_name='Template ID')),
                ('emails', models.JSONField(verbose_name='Emails')),
                ('hourly_rate', models.FloatField(blank=True, null=True, verbose_name='Hourly Rate')),
                ('executive_summary', models.TextField(verbose_name='Executive Summary')),
                ('scope_of_work', models.TextField(verbose_name='Scope of Work')),
                ('deliverables', models.TextField(verbose_name='Deliverables')),
                ('queries_assumption', models.TextField(verbose_name='Queries & Assumption')),
                ('technology_allocation', models.JSONField(verbose_name='Technology Allocation')),
                ('other_resources', models.JSONField(blank=True, null=True, verbose_name='Other Resources')),
                ('qa_percentage', models.FloatField(blank=True, null=True, verbose_name='QA Percentage')),
                ('reference', models.JSONField(blank=True, null=True, verbose_name='Reference')),
                ('reference_documents', models.JSONField(blank=True, null=True, verbose_name='Reference Documents')),
            ],
        ),
    ]
