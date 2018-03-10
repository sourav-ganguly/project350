from django import forms
from.models import Comment


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        max_length=3000,
        widget=forms.Textarea,
        required=True,
        label='Question'
    )
    course_code = forms.CharField(
        max_length=20,
        required=True,
        label='Course Code'
    )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_text',)
