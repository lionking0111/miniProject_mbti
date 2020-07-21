from django.urls import path 
from . import views

urlpatterns = [   
    path('index_초기설정/',views.index),
    path('mbti1/',views.mbti1),
    path('mbti_exam1/',views.mbti_exam1),
    path('show_result/',views.showResult, name='show_result'),
    
]
