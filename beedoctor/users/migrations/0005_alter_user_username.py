# Generated by Django 4.1.9 on 2023-06-08 03:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_user_social_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(default="", max_length=150, verbose_name="username"),
        ),
    ]
