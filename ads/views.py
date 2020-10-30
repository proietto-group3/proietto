from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin as BaseLoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from django.urls import reverse


from ads.models import Ad
from ads.forms.adeditform import EditAdForm

class LoginRequiredMixin(BaseLoginRequiredMixin):
    def get_login_url(self):
        return reverse("login")

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

class EditAdView(LoginRequiredMixin, UpdateView):
    template_name = 'ads/ad_edit.html'
    form_class = EditAdForm
    model = Ad

    def get_success_url(self):
        pk = self.kwargs["pk"]
        slug = self.kwargs['slug']
        messages.success(request=self.request, message="Edit success!")
        return reverse_lazy("ads:ad_detail.html", kwargs={'pk': pk, 'slug': slug})
