from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('enviados/', views.sent_box, name='sent_box'),
    path('<int:pk>/', views.message_detail, name='message_detail'),
    path('enviar/', views.message_send, name='message_send'),
    path('<int:pk>/eliminar/', views.message_delete, name='message_delete'),
]
