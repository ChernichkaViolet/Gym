#
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from core.models import Profile


def profile_show(request, pk, template_name='my_profile.html'):
    context = {}
    profile = get_object_or_404(Profile, pk=pk)
    context['profile'] = profile
    return render(request, template_name, context)

# def server_create(request, template_name='servers/server_form.html'):
#     form = ServerForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('server_list')
#     return render(request, template_name, {'form':form})


def profile_update(request, pk ):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = forms.ProfileUpdateForm(request.POST or None, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('myaccount:profile',pk)
    else:
        form = forms.ProfileUpdateForm(instance=profile)
    return render(request,'my_profile_edit.html', {'form': form})

# def server_delete(request, pk, template_name='servers/server_confirm_delete.html'):
#     server = get_object_or_404(Server, pk=pk)
#     if request.method=='POST':
#         server.delete()
#         return redirect('server_list')
#     return render(request, template_name, {'object':server})