# Generated by Django 4.1.7 on 2023-04-07 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_attemptquiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='attemptquiz',
            name='right_ans',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='attemptquiz',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.student'),
        ),
    ]
