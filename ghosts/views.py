from django.shortcuts import render, redirect
from ghosts.models import GhostName, GhostUser
from ghosts.forms import NamePickerForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request):
    """
    Home page for blogs site
    """
    context = {
        'ghost_names': GhostName.objects.all(),
    }

    return render(request, 'ghosts/index.html', context)


def name_picker(request):

    name_picker_form = NamePickerForm(request.POST or None)

    ghost_user = None
    if request.user:
        try:
            ghost_user = GhostUser.objects.get(user=request.user)
        except ObjectDoesNotExist:
            # log the exception if needed
            pass

    if name_picker_form.is_valid():
        obj = name_picker_form.save(commit=False)
        obj.user = request.user
        obj.user.first_name = name_picker_form.cleaned_data['first_name']
        obj.user.last_name = name_picker_form.cleaned_data['last_name']
        obj.user.save()
        obj.save()
        redirect('home')

    context = {
        'name_picker_form': name_picker_form,
        'ghost_user': ghost_user
    }

    return render(request, 'ghosts/name_picker.html', context)



