# Generated by Django 3.1.6 on 2021-02-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_objec', models.CharField(max_length=300)),
                ('date_of_start', models.DateField()),
                ('date_of_end', models.DateField()),
                ('address', models.CharField(max_length=400)),
                ('users_how_can_work', models.CharField(max_length=300)),
            ],
        ),
    ]
