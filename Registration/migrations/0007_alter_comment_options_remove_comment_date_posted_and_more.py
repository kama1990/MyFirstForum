# Generated by Django 4.2.2 on 2023-06-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0006_alter_comment_options_remove_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
