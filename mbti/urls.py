from django.urls import path 
from . import views                 #url/뷰 맵핑

urlpatterns = [   
    path('',views.intro),
    path('signin/',views.signin),
    path('signin/q1/',views.Crawling_Image),
    path('result/',views.result),
    path('info_inquiry/', views.info_inquiry),
    path('show_result/',views.showResult, name='show_result'),
    path('q<int:num>/', views.question, name='question'),
]
