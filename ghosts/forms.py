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
        instance = kwargs.get('instance', None)
        super(NamePickerForm, self).__init__(*args, **kwargs)
        self.fields['ghost_name'].queryset = GhostName.objects.filter(ghostuser__isnull=True)
        if instance:
            self.initial['first_name'] = instance.user.first_name
            self.initial['last_name'] = instance.user.last_name
