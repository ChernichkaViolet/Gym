from django import forms
from django.utils.translation import ugettext as _

from . import models


class ExerciseCreate(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Описание'),
        required=False
    )
    set_quantity = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Подходы'),
        required=False
    )
    repeats = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Повторения'),
        required=False
    )
    created_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Дата создания'),
        required=False
    )

    class Meta:
        model = models.Exercise
        fields = [
            'description',
            'set_quantity',
            'repeats',
            'created_date'
        ]


class ExerciseUpdate(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Цель на ближайшие 3 месяца'),
        required=False
    )
    set_quantity = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Цель на ближайшие 3 месяца'),
        required=False
    )
    repeats = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Цель на ближайшие 3 месяца'),
        required=False
    )
    create_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label=_('Цель на ближайшие 3 месяца'),
        required=False
    )

    class Meta:
        model = models.Exercise
        fields = [
            'description',
            'set_quantity',
            'repeats',
            'created_date'
        ]