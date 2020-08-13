from django.shortcuts import render, redirect
from ghosts.models import GhostName, GhostUser
from ghosts.forms import NamePickerForm, NameUpdateForm
from ghosts.utils import get_ghost_user

# Create your views here.


def home(request):
    """
    Home page for blogs site
    """
    context = {
        'ghost_names': GhostName.objects.all(),
        'ghost_user': get_ghost_user(request),
    }

    return render(request, 'ghosts/index.html', context)


def name_picker(request):
    """
    Create ghost user
    """
    name_picker_form = NamePickerForm(request.POST or None)
    ghost_user = get_ghost_user(request)

    if name_picker_form.is_valid():
        obj = name_picker_form.save(commit=False)
        obj.user = request.user
        obj.user.first_name = name_picker_form.cleaned_data['first_name']
        obj.user.last_name = name_picker_form.cleaned_data['last_name']
        obj.user.save()
        obj.save()
        return redirect('home')

    if ghost_user:
        name_picker_form = NameUpdateForm(instance=ghost_user)

    context = {
        'name_picker_form': name_picker_form,
        'ghost_user': ghost_user
    }

    return render(request, 'ghosts/name_picker.html', context)


def update_ghost_name(request):
    """
    Update exisiting ghost user's name
    """
    ghost_user = get_ghost_user(request)
    name_update_form = NameUpdateForm(request.POST, instance=ghost_user)
    if name_update_form.is_valid():
        name_update_form.save()
        return redirect('home')

    return redirect('name_picker')
