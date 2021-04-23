from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',views.ArticleViewSet,basename='article')


urlpatterns = [
    path('viewset/',include(router.urls)),
    path('detail/<int:pk>/',views.article_detail,name='detail'),
    path('article/', views.article_list, name='article'),
    path('apiview/',views.ArticleAPIView.as_view()),
    path('genericview/<int:id>/',views.GenericAPIView.as_view()),

]
