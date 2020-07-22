from django.urls import path 
from . import views

urlpatterns = [   
    path('',views.intro),
    path('signin/',views.signin),
    path('signin/q1/',views.q1),
    path('signin/q2/',views.q2),
    path('signin/q3/',views.q3),
    path('signin/q4/',views.q4),
    path('signin/q5/',views.q5),
    path('signin/q6/',views.q6),
    path('signin/q7/',views.q7),
    path('signin/q8/',views.q8),
    path('signin/result/',views.result),
    path('info_inquiry/', views.info_inquiry),
    path('show_result/',views.showResult, name='show_result'),
    path('sign/',views.id_overlap_check, name='id_overlap_check')
]
