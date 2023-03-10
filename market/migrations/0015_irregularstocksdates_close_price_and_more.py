# Generated by Django 4.1.4 on 2023-01-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0014_alter_stocklist_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='irregularstocksdates',
            name='close_price',
            field=models.DecimalField(decimal_places=6, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='irregularstocksdates',
            name='open_price',
            field=models.DecimalField(decimal_places=6, max_digits=16, null=True),
        ),
    ]
