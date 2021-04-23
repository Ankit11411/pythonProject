from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("mysite/<int:question_id>/", views.page, name='page'),
    path("bbb/", views.ListQuestionApiview.as_view(), name="todo_list"),
    path("ccc/", views.ListQuestion.as_view(), name="List_view"),
]
