from django.contrib import admin
from django.urls import path, include
from mbti import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mbti/', include('mbti.urls'))
]
