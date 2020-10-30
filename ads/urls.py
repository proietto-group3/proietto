from django.urls import path
from ads.views import AllAdsListView

app_name = 'ads'

urlpatterns = [


    path('all/', AllAdsListView.as_view(), name='all_ads_list'),


]