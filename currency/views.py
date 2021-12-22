from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View

from currency.models import Source, Rate, ContactUs
from currency.forms import RateForm, SourceForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings


class RateListView(ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    form_class = RateForm
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'

    class MyView(UserPassesTestMixin, View):

        def test_func(self):
            return self.request.user.email.endswith('@example.com')


class RateDetailsView(DetailView):
    model = Rate
    template_name = 'rate_details.html'

    # def get_object(self, queryset=None):
    #     return self.request.user


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'

    class MyView(UserPassesTestMixin, View):

        def test_func(self):
            return self.request.user.email.endswith('@example.com')


def main(request):
    return render(request, "main.html")


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_c.html'


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_u.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_d.html'


class SourceDetailsView(DetailView):
    model = Source
    template_name = 'source_details.html'


class ContactUsCreateView(CreateView):
    model = ContactUs
    success_url = reverse_lazy('main')
    template_name = 'contactus_create.html'
    fields = (
        'name',
        'reply_to',
        'subject',
        'body',
    )

    def _send_email(self):
        subject = 'User ContactUs'
        body = f'''
            Request from: {self.object.name}
            Email to reply: {self.object.reply_to} 
            Subject: {self.object.subject}
    
            Body: {self.object.body}
        '''

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ['danikmoiseenkov1@gmail.com'],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect





