# Generated by Django 4.2.2 on 2023-07-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_vacancy_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=55)),
            ],
        ),
        migrations.AddField(
            model_name='vacancy',
            name='employment_type',
            field=models.CharField(choices=[('full_time', 'Full time'), ('part_time', 'Part time'), ('piecework', 'Piecework')], default='full_time', max_length=20),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='skills',
            field=models.ManyToManyField(to='core.skill'),
        ),
    ]
