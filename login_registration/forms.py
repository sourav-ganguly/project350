from django import forms


class RegistrationForm(forms.Form):
    question_text = forms.CharField(
        max_length=3000, widget=forms.Textarea, required=True, label='Question')
    user = forms.CharField(max_length=20, required=True, label='User Name')
    password = forms.CharField(max_length=20, required=True, label='User Name')
    ser = forms.CharField(max_length=20, required=True, label='User Name')
