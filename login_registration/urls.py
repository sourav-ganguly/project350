from django.urls import path, re_path

from . import views

app_name = 'login_registration'
urlpatterns = [
    re_path(r'.*', views.register, name="registration"),
]
