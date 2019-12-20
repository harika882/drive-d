# Generated by Django 2.2.3 on 2019-07-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=400)),
                ('payment_mode', models.CharField(max_length=400)),
                ('payment_data', models.CharField(max_length=200)),
                ('items', models.TextField()),
                ('fulfilled', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=800)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=800)),
                ('imglink', models.CharField(max_length=200)),
            ],
        ),
    ]
