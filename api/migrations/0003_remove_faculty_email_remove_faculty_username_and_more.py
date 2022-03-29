# Generated by Django 4.0.3 on 2022-03-29 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_journal_conference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='email',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='username',
        ),
        migrations.AddField(
            model_name='faculty',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='faculty_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
