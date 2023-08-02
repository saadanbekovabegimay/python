from django.urls import path
from .views import *

urlpatterns = [
    path('list/', news_list, name='news-list'),
    path('detail/<int:id>/', news_detail, name='news-detail'),
    path('create/', ArticleCreateView.as_view(), name='create-article'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update-article'),
]
