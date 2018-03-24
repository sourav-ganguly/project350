from django.urls import path, re_path

from . import views

app_name = 'qb_admin'
urlpatterns = [
    # path('', views.detail, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.get_question_accept_delete),
]
