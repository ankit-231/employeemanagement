from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

    path('get_user/', views.get_user, name='get_user'),
    path('check/', views.check, name='check'),
    path('post_user/', views.post_user, name='post_user'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('post_role/', views.post_role, name='post_role'),
    path('edit_role/<int:pk>', views.edit_role, name='edit_role'),
    
    ]