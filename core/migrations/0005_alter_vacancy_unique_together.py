# Generated by Django 4.2.2 on 2023-07-07 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_company'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vacancy',
            unique_together={('title', 'email')},
        ),
    ]
