from django import forms
import communication_app.models


class PetForm(forms.ModelForm):
    class Meta:
        model = communication_app.models.Pet
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-control'})

class UpdateForm(forms.ModelForm):
    class Meta:
        model = communication_app.models.Update
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget = forms.TextInput(attrs={
            'class': 'form-control'})
