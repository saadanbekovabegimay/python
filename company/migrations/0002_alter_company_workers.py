# Generated by Django 4.2.2 on 2023-07-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_resume'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='workers',
            field=models.ManyToManyField(blank=True, related_name='company', to='worker.worker'),
        ),
    ]
