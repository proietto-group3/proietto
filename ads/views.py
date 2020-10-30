from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from ads.models import Ad


class AllAdsListView(ListView):
    template_name = 'ads/ads_list.html'
    model = Ad
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')


class AdDetailView(DetailView):
    template_name = 'ads/ad_detail.html'
    model = Ad

    def get_success_url(self):
        pk = self.kwargs["pk"]
        slug = self.kwargs['slug']
        return reverse_lazy('news:article_detail', kwargs={'pk': pk, 'slug': slug})
