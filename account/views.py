from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView

from account.forms import UserSignUpForm
from account.models import User


class UserSignUpView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('main')
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        user = User.objects.filter(username=username).only('id').first()
        if user:
            user.is_active = True
            user.save(update_fields=['is_active'])
        url = super().get_redirect_url()
        return url


class ProfileView(LoginRequiredMixin, UpdateView):
    # model = get_user_model()
    queryset = get_user_model().objects.all()
    success_url = reverse_lazy('main')
    template_name = 'profile.html'
    fields = (
        'first_name',
        'last_name',
        'avatar',
    )

    def get_object(self, queryset=None):
        return self.request.user