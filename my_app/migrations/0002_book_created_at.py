# Generated by Django 5.1.6 on 2025-03-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
