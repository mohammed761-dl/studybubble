# Generated by Django 5.2.3 on 2025-06-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='group_files/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='group_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
