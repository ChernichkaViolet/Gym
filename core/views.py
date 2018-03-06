from datetime import timedelta

from django.shortcuts import redirect
from django.utils.timezone import now
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.db import transaction

from . import models, forms
from core import tasks


class RegisterView(FormView):
    form_class = forms.RegisterForm
    template_name = 'register_form.html'
    success_url = reverse_lazy('login')

    @staticmethod
    def save_and_activate_user(**kwargs):

        profile = models.Profile(
            username=kwargs['username'],
            password=kwargs['password1'],
            email=kwargs['email'],
            is_active=False
        )
        profile.set_password(profile.password)
        profile.save()
        site_settings = models.SiteSettings.get_solo()
        activation = models.Activation(
            valid_until=now() + timedelta(hours=site_settings.activation_url_preiod)
        )
        activation.set_url()
        activation.save()
        profile.activation = activation
        profile.save()

        return profile

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():

            with transaction.atomic():
                try:
                    profile = self.save_and_activate_user(**form.cleaned_data)
                except Exception as exc:
                    messages.error(
                        request,
                        _('Не удалось создать учётную запись. Обратитесь к администратору.')
                    )
                    raise exc
                else:
                    messages.success(
                        request,
                        _('Учётная запись успешно создана. Уведомление в ящике.')
                    )
                    tasks.send_activation_email_task(
                        profile.pk, self.request.META['HTTP_HOST']
                    )
                    from django.forms import model_to_dict
                    # send_activation_email(profile, self.request.META['HTTP_HOST'])
                    tasks.send_activation_email_task.delay(profile.pk, self.request.META['HTTP_HOST'])

            return self.form_valid(form)

        return self.form_invalid(form)


class ActivateView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        try:
            activation = models.Activation.objects.get(url__icontains=token)
        except models.Activation.DoesNotExist:
            messages.error(
                request,
                _('Не удалось активировать учётную запись.')
            )
            return redirect('register')

        activation.profile.is_active = True
        activation.profile.save()

        return super(ActivateView, self).get(request, *args, **kwargs)


