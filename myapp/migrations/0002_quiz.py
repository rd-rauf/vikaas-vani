# Generated by Django 4.0.3 on 2024-07-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=20)),
                ('b', models.CharField(max_length=20)),
                ('d', models.CharField(max_length=20)),
                ('que', models.CharField(choices=[(1, models.CharField(max_length=20)), (2, models.CharField(max_length=20)), (3, models.CharField(max_length=20)), (4, models.CharField(max_length=20))], max_length=100)),
            ],
        ),
    ]
