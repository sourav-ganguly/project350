from django.db import models
from django.forms import ModelForm


class Question(models.Model):
    question_text = models.TextField(max_length=3000)
    user = models.CharField(max_length=20)
    pub_date = models.DateTimeField("Date published")

    def __str__(self):
        return self.question_text

# class QuestionForm(ModelForm):
#     class Meta:
#         model = Question
#         fields = ['question_text', 'user', 'pub_date']
