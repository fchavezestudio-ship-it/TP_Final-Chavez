from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.ProfileDetailView.as_view(), name='profile'),
    path('perfil/editar/', views.profile_edit, name='profile_edit'),
    path('perfil/cambiar-password/', views.change_password, name='change_password'),
]
