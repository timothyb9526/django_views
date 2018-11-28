from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('add/', views.Add.as_view(), name='add'),
]
