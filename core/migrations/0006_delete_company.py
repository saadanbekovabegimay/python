# Generated by Django 4.2.2 on 2023-07-10 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_vacancy_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]
