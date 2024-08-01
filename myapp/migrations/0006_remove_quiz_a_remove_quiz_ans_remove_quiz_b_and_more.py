# Generated by Django 4.0.3 on 2024-07-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_quiz_correct_ans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='a',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='ans',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='b',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='c',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='correct_ans',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='d',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='que',
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct_option',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='field_of_study',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='option1',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='option2',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='option3',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='option4',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='question_text',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]