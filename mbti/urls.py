from django.urls import path 
from . import views                 #url/뷰 맵핑

urlpatterns = [   
    path('',views.intro),
    path('signin/',views.signin),

    path('signin/result/',views.result),
    path('info_inquiry/', views.info_inquiry),
    path('show_result/',views.showResult, name='show_result'),
    path('signin/q<int:num>/', views.question, name='question'),
    path('sign/',views.id_overlap_check, name='id_overlap_check')
]
