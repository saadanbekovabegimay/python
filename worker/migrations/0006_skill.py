# Generated by Django 4.2.2 on 2023-07-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0005_resume_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=55)),
            ],
        ),
    ]