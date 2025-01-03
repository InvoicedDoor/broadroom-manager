# Generated by Django 5.0.6 on 2024-05-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broadroom',
            fields=[
                ('broadroom_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
