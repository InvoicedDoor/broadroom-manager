# Generated by Django 5.0.6 on 2024-12-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_enrollmentcounter_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=70, null=True, unique=True),
        ),
    ]