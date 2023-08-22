# Generated by Django 4.2.4 on 2023-08-21 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_postlike_post_alter_postlike_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.post'),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]