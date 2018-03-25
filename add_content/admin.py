from django.contrib import admin
from .models import Question, Comment, Course, UserDetail, LogTable

# Register your models here.
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Course)
admin.site.register(UserDetail)
admin.site.register(LogTable)
