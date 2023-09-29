# Generated by Django 4.2.5 on 2023-09-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='seed',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='seed',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]