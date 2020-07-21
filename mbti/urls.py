from django.urls import path 
from . import views

urlpatterns = [   
    path('',views.intro),
    path('signin/',views.signin),
    path('q1/',views.Question),
    path('result/',views.result),
    path('inquiry/',views.inquiry),
    path('show_result/',views.showResult, name='show_result')
    
]
