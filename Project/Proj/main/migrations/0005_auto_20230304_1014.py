# Generated by Django 3.0.14 on 2023-03-04 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230303_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='username',
            new_name='full_name',
        ),
    ]
