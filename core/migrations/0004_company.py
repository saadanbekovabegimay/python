# Generated by Django 4.2.2 on 2023-06-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_alter_vacancy_options_vacancy_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('num_worker', models.IntegerField(null=True)),
                ('is_hunting', models.BooleanField(default=True)),
            ],
        ),
    ]