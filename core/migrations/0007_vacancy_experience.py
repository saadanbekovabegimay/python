# Generated by Django 4.2.2 on 2023-07-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
