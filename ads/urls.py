from django.urls import path
from ads.views import AdDetailView, AllAdsListView

app_name = 'ads'

urlpatterns = [


    path('all/', AllAdsListView.as_view(), name='all_ads_list'),

    path('show_ad/<int:pk>/<slug:slug>', AdDetailView.as_view(), name='ad_detail'),


]