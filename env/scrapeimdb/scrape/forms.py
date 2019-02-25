from django import forms


class UrlForm(forms.Form):
    url_link = forms.URLField(label='Paste your url here')
