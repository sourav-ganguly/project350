from django.contrib import admin
from .models import Question, Comment, Course, UserDetail, LogTable
from .models import UserGroup, Chapter, RoleTable

# Register your models here.
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Course)
admin.site.register(UserDetail)
admin.site.register(LogTable)
admin.site.register(UserGroup)
admin.site.register(Chapter)
admin.site.register(RoleTable)
