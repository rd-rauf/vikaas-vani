# Generated by Django 4.0.3 on 2024-07-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_report_totalemarks_alter_report_totalfmarks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='field',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
