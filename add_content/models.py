from django.db import models
from django.forms import ModelForm
from django.conf import settings


class Question(models.Model):
    question_text = models.TextField(max_length=3000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    pub_date = models.DateTimeField("Date published")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.question_text


class Comment(models.Model):
    comment_text = models.TextField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    created_date = models.DateTimeField("Date published")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.comment_text
