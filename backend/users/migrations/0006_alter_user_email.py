# Generated by Django 5.0.6 on 2024-12-23 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_date_joined_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]
