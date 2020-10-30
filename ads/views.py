from django.shortcuts import render
from django.views.generic import ListView
from ads.models import Ad


class AllAdsListView(ListView):
    template_name = 'ads/ads_list.html'
    model = Ad
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')