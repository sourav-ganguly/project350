from django.urls import path, re_path

from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('me/', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/', views.get_detail_view_with_comment, name='detail'),
    re_path('add/*', views.get_question, name='add_question')
]
