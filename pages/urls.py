from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('crear/', views.post_create, name='post_create'),
    path('<int:pk>/editar/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/eliminar/', views.post_delete, name='post_delete'),
]
