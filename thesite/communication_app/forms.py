from django import forms
import communication_app.models


class PetForm(forms.ModelForm):
    class Meta:
        model = communication_app.models.Pet
        fields = ['name']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = communication_app.models.Update
        fields = ['text']
