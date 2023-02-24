# Generated by Django 4.1.7 on 2023-02-24 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=300)),
                ('type_plans', models.CharField(max_length=50)),
                ('road_map', models.CharField(max_length=300)),
                ('duration', models.IntegerField(default=0)),
                ('value', models.FloatField(default=0.0)),
            ],
        ),
    ]
