import os
import django
django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App.settings')
from market.models import Stock, IrregularStocksDates, StockList

# def Del_Inc(ticker):
    # print(Stock.objects.filter(ticker=ticker))
    # Stock.objects.filter(ticker=ticker).delete()
    # IrregularStocksDates.objects.filter(ticker=ticker).delete()
    # StockList.objects.filter(ticker=ticker).delete()
# Del_Inc('OCEA')


# def Del_Inc(ticker):
#     print(Stock.objects.filter(ticker=ticker))
#     Stock.objects.filter(ticker=ticker).delete()
#     IrregularStocksDates.objects.filter(ticker=ticker).delete()
#     StockList.objects.filter(ticker=ticker).delete()
# Del_Inc('OCEA')


# def Del_StockNames():
#     StockNames.objects.all().delete()
# Del_StockNames()