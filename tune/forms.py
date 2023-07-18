from django import forms
from .models import Tune

class TuneForm(forms.ModelForm):

    class Meta:
        model = Tune
        fields = (
            'name',
            'key',
            'fiddler',
            'tuning',
            'state',
            'description',
            'stars',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-input', 'placeholder': 'Name', 'autofocus': True, 'onfocus': 'this.setSelectionRange(this.value.length, this.value.length)'}
        )
        self.fields['key'].widget.attrs.update(
            {'class': 'form-input'}
        )
        self.fields['fiddler'].widget.attrs.update(
            {'class': 'form-input', 'placeholder': 'Fiddler'}
        )
        self.fields['tuning'].widget.attrs.update(
            {'class': 'form-input'}
        )
        self.fields['state'].widget.attrs.update(
            {'class': 'form-input', 'placeholder': 'State'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-input', 'placeholder': 'Description'}
        )
        self.fields['stars'].widget.attrs.update(
            {'class': 'form-input', 'min': 1, 'max': 5, 'value': 5}
        )
