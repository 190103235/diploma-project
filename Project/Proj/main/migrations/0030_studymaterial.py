# Generated by Django 4.1.7 on 2023-04-09 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_attemptquiz_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('upload', models.FileField(null=True, upload_to='study_materials/')),
                ('remarks', models.TextField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
            options={
                'verbose_name_plural': '12. Study Materials',
            },
        ),
    ]
