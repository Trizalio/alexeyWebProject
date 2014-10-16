from django import forms

class questionForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(widget=forms.Textarea, max_length=200)


class answerForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, max_length=200)
