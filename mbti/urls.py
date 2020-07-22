from django.urls import path 
from . import views

urlpatterns = [   
    path('',views.intro),
    path('signin/',views.signin),
    path('signin/q1/',views.Crawling_Image),
    path('signin/q2/',views.Crawling_Image),
    path('signin/q3/',views.signin0),
    path('signin/q4/',views.signin1),
    path('signin/q5/',views.signin2),
    path('signin/q6/',views.signin3),
    path('signin/q7/',views.signin4),
    path('signin/q8/',views.signin5),
    path('result/',views.result),
    path('info_inquiry/', views.info_inquiry),
    path('show_result/',views.showResult, name='show_result')
    
]
