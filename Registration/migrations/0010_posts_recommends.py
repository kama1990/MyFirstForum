# Generated by Django 4.2.2 on 2023-07-03 14:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registration', '0009_comment_image_posts_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='recommends',
            field=models.ManyToManyField(blank=True, related_name='recommend', to=settings.AUTH_USER_MODEL),
        ),
    ]