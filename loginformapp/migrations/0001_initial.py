# Generated by Django 3.0.6 on 2020-05-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
