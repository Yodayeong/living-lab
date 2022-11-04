from django.urls import path
from . import views

app_name = "grandchildren"

urlpatterns = [
    path('', views.index, name="index"),
    path('sentiment/', views.sentiment, name="sentiment"),
    path('setting/', views.setting, name="setting"),
]
