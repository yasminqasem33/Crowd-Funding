from django import forms


class Form_comment(forms.Form):
  text = forms.CharField(widget=forms.Textarea,label='text', max_length=1000)

class Form_donation(forms.Form):
    donation = forms.IntegerField(label='donation')
class Form_reportProject(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='text', max_length=1000)
class Form_reportComment(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='text', max_length=1000)