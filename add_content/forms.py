from django import forms
from.models import Comment, Course


class QuestionForm(forms.Form):
    question_name = forms.CharField(
        max_length=300,
        widget=forms.Textarea,
        required=True,
        label='Question name'
    )
    question_text = forms.CharField(
        max_length=3000,
        widget=forms.Textarea,
        required=True,
        label='Question description'
    )
    COURSE_CHOICES = [(course.course_code, course.course_code + "- Class " +
                       course.class_no + ", " + course.subject)
                      for course in Course.objects.all()]
    course_code = forms.CharField(
        max_length=20,
        required=True,
        label='Course Code',
        widget=forms.Select(choices=COURSE_CHOICES),
    )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_text',)
