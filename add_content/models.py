from django.db import models
from django.forms import ModelForm
from django.conf import settings
ACCEPTED = "ACCEPTED"
PENDING = "PENDING"
DISCARDED = "DISCARDED"
OUTDATED = "OUTDATED"
USED = "USED"
DELETED = "DELETED"


class Course(models.Model):
    course_code = models.CharField(max_length=10)
    class_no = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.course_code


class Question(models.Model):
    question_name = models.TextField(max_length=300, null=True)
    question_text = models.TextField(max_length=3000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    pub_date = models.DateTimeField("Date published")

    STATUS_CHOICES = (
        (ACCEPTED, "Accepted"),
        (PENDING, "Pending"),
        (DISCARDED, "Discarded"),
        (OUTDATED, "Outdated"),
        (USED, "Used"),
        (DELETED, "Deleted"),
    )
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default=PENDING,
        null=True,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.question_text


class Comment(models.Model):
    comment_text = models.TextField(max_length=100)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        null=True,
    )
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

