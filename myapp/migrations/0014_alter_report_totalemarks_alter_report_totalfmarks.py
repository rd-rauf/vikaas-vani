# Generated by Django 4.0.3 on 2024-07-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_techcourse_ngo_note_alter_report_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='totalEMarks',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='totalFMarks',
            field=models.FloatField(blank=True, null=True),
        ),
    ]