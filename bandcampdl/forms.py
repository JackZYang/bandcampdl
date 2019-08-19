from django import forms

class getURL(forms.Form):
    url = forms.URLField(label='url', widget=forms.URLInput(attrs={'placeholder':'Enter URL'}))