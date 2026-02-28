from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_page, name='chat_page'),
    path('api/message/', views.chat_view, name='chat_api'),
    path('api/diagnose/', views.diagnose_symptoms, name='diagnose_api'),
]