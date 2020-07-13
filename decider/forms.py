from django import forms

from decider.models import Item


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'text', 'file']


class AddItemFormSave(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'text', 'file', 'campaign']
