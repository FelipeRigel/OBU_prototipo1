from django import forms

class NameForm(forms.Form):
    data = forms.CharField(label='Json', max_length=300)