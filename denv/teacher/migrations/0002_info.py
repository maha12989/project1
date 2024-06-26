# Generated by Django 5.0.4 on 2024-04-22 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('salary', models.PositiveIntegerField()),
                ('blood_group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teacher.blood_group')),
            ],
            options={
                'ordering': ['-salary'],
            },
        ),
    ]
