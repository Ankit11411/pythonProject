from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("home/", views.index, name='index'),
    path("<int:question_id>/", views.detail, name='detail'),
    path("aaa/", views.fetch, name='fetch'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path("polls/<int:question_id>/", views.detail, name='detail2')
]
