# Generated by Django 4.1.7 on 2023-04-15 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_rename_teacheruserchant_teacheruserchat'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='facebook_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='instagram_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='twitter_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='website_url',
            field=models.URLField(null=True),
        ),
    ]