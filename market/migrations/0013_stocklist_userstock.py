# Generated by Django 4.1.4 on 2023-01-06 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0012_alter_irregularstocksdates_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='UserStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.stocklist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
