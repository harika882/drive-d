# Generated by Django 2.1.5 on 2019-08-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='short_urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=20)),
                ('long_url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
    ]