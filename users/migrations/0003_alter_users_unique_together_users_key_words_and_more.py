# Generated by Django 4.1.4 on 2023-01-02 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_remove_users_username_alter_profile_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='users',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='users',
            name='key_words',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='tickers',
            field=models.TextField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
    ]