from django.urls import reverse_lazy
from django.shortcuts import render


from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from . import models , forms


# class ExercisesList(ListView): #SingleObjectMixin
#     model = models.
#     template_name = 'exercises_list.html'


def exercises_list(request):
    context = {}
    exercises_list = models.Exercise.objects.all()
    context.update({'exercises_list': exercises_list})
    return render(
        request,
        'exercises_list.html',
        context=context
    )


class ExercisesCreate(CreateView):
    model = models.Exercise
    form_class = forms.ExerciseCreate
    template_name = 'exercises_create.html'
    success_url = reverse_lazy('exercises:list')


class ExercisesDetail(DetailView):   #SingleObjectMixin,
    model = models.Exercise
    template_name = 'exercises_detail.html'


class ExercisesUpdate(UpdateView):
    model = models.Exercise
    template_name = 'exercises_update.html'
    success_url = reverse_lazy('exercises:list')
    form_class = forms.ExerciseUpdate


class ExercisesDelete(DeleteView):
    model = models.Exercise
    success_url = reverse_lazy('exercises:list')

