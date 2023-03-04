import csv
import os
import django
from market.models import StockNames
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App.settings')
django.setup()

import csv
with open('NYSE_list.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        symbol = row.get('Symbol')
        name = row.get('Name')
        sector = row.get('Sector')
        industry = row.get('Industry')
        country = row.get('Country')

        if country in [None, 'United States'] and symbol and name:
            stock, created = StockNames.objects.get_or_create(ticker=symbol, name=name, defaults={'sector': sector, 'industry': industry})
            if not created:
                stock.sector = sector
                stock.industry = industry
                stock.save()



