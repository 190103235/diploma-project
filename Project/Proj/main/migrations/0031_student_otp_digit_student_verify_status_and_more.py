# Generated by Django 4.1.7 on 2023-04-13 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_studymaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='otp_digit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='verify_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='otp_digit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='verify_status',
            field=models.BooleanField(default=False),
        ),
    ]