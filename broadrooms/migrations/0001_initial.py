# Generated by Django 5.0.6 on 2024-05-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broadroom',
            fields=[
                ('broadroom_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=False)),
            ],
        ),
    ]
