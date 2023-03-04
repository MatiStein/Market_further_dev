# Generated by Django 4.1.4 on 2023-02-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0015_irregularstocksdates_close_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('industry', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('ticker', 'name')},
            },
        ),
    ]