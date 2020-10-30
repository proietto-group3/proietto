from django.urls import path
from ads.views import AddAdView, AdDetailView, AllAdsListView, EditAdView, AdDeleteView

app_name = 'ads'

urlpatterns = [
    path('add/', AddAdView.as_view(), name='add_ad'),
    path('edit/<int:pk>/<slug:slug>', EditAdView.as_view(), name='edit_ad'),
    path('delete/<int:pk>/<slug:slug>', AdDeleteView.as_view(), name='delete_ad'),


    path('all/', AllAdsListView.as_view(), name='all_ads_list'),
    path('show_ad/<int:pk>/<slug:slug>', AdDetailView.as_view(), name='ad_detail'),


]