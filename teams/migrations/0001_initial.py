# Generated by Django 2.2.1 on 2019-05-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
