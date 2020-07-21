from django.urls import path 
from . import views

urlpatterns = [   
    path('',views.intro),
    path('signin/',views.signin),
    path('q1/',views.question),
    path('result/',views.result),
    path('show_result/',views.showResult, name='show_result'),
    
]
