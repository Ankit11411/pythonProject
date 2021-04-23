from . import views
from django.urls import path

urlpatterns = [
    path('detail/<int:pk>/',views.article_detail,name='detail'),
    path('article/', views.article_list, name='article'),

]
