# Generated by Django 4.2.11 on 2024-04-12 12:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('logo', models.ImageField(blank=True, upload_to='templates/logos/')),
                ('banner', models.ImageField(blank=True, upload_to='templates/banners/')),
                ('back_cover', models.ImageField(blank=True, upload_to='templates/back_covers/')),
                ('back_cover_logo', models.ImageField(blank=True, upload_to='templates/back_cover_logos/')),
                ('preview_url', models.URLField(blank=True, max_length=1024)),
                ('footer', models.TextField(blank=True)),
                ('footer_link', models.URLField(blank=True, max_length=1024, null=True)),
                ('introduction', models.TextField(blank=True)),
                ('companyName', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('is_default', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='templates', to='client.client')),
            ],
        ),
    ]
