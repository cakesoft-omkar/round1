from django.urls import path
from project import views

urlpatterns = [
    path('', views.index1),
    path('question/', views.index2, name='index2'),
    path('question/answer/<int:qno>/', views.index3,name='index3'),
]
