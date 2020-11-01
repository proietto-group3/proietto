from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin as BaseLoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from ads.forms.adform import AdForm
from ads.models import Ad


class LoginRequiredMixin(BaseLoginRequiredMixin):
    def get_login_url(self):
        return reverse("login")


class AddAdView(LoginRequiredMixin, CreateView):
    model = Ad
    template_name = 'ads/add_ad.html'
    form_class = AdForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(request=self.request, message='Your ad has been added.')
        return super().form_valid(form)


class EditAdView(LoginRequiredMixin, UpdateView):
    template_name = 'ads/ad_edit.html'
    form_class = AdForm
    model = Ad

    def get_success_url(self):
        pk = self.kwargs["pk"]
        slug = self.kwargs['slug']
        messages.success(request=self.request, message="Edit success!")
        return reverse_lazy("ads:ad_detail", kwargs={'pk': pk, 'slug': slug})


class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    template_name = 'ads/ad_delete.html'

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False

    def get_success_url(self):
        messages.success(request=self.request, message="You successfuly deleted ad!")
        return reverse_lazy('ads:all_ads_list')


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
        return reverse_lazy('ads:article_detail', kwargs={'pk': pk, 'slug': slug})


class TagAdListView(ListView):
    template_name = 'ads/tag_ad_list.html'
    model = Ad
    queryset = Ad.objects.order_by('-pk')
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            tags__slug=self.kwargs['slug'])

    def ad_tag(self):
        return get_object_or_404(Ad.tags, slug=self.kwargs['slug'])
