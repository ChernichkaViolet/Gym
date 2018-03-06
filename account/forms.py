from django import forms
from django.utils.translation import ugettext as _

from core.models import Profile


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Имя '),
        required=False
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Фамилия'),
        required=False
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('День Рождения'),
        required=False
    )
    purpose = forms.CharField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Цель на ближайшие 3 месяца'),
        required=False
    )

    class Meta:
        model = Profile
        fields = (
            'avatar',
            # 'username',
            'first_name',
            'last_name',
            'birth_date',
            'purpose'
        )

