from django import forms
from.models import Comment


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        max_length=3000, widget=forms.Textarea, required=True, label='Question')
    user = forms.CharField(max_length=20, required=True, label='User Name')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_text',)