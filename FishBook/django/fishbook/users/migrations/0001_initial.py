# Generated by Django 3.0.6 on 2020-06-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=20)),
                ('userPw', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('rrn', models.CharField(max_length=200)),
                ('last_destination', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
