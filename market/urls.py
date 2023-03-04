from django.urls import path
from . import views


urlpatterns = [
    path('stocks/', views.stocks_list),
    path('analyzed/', views.Stock_Analyze),
    path('get_data/',views.get_data),
    path('analyze_query/',views.analyze_volume_query),
    path('ticker_list', views.ticker_list),
    path('get_top_3_ratings', views.get_top_3_ratings),
    path('get_latest_3_ratings', views.get_latest_3_ratings),
    path('get_name_from_ticker/', views.get_name_from_ticker),
    path('user_ticker', views.add_user_stock)
    
    ]