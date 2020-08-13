from ghosts.models import GhostUser, GhostName
from django.forms import ModelForm
from django import forms


class NamePickerForm(ModelForm):

    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)

    class Meta:
        model = GhostUser
        fields = ['ghost_name']

    def __init__(self, *args, **kwargs):
        super(NamePickerForm, self).__init__(*args, **kwargs)
        self.fields['ghost_name'].queryset = GhostName.objects.filter(ghostuser__isnull=True)


class NameUpdateForm(ModelForm):

    class Meta:
        model = GhostUser
        fields = ['ghost_name']

    def __init__(self, *args, **kwargs):
        super(NameUpdateForm, self).__init__(*args, **kwargs)
        self.fields['ghost_name'].queryset = GhostName.objects.filter(ghostuser__isnull=True)
