from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

    path('home/', views.home_view, name='home_view'),

    path('get_user/', views.get_user, name='get_user'),
    path('check/', views.check, name='check'),
    path('post_user/', views.post_user, name='post_user'),
    path('edit_user/', views.edit_user, name='edit_user'),
    
    path('get_role/', views.get_role, name='get_role'),
    path('post_role/', views.post_role, name='post_role'),
    path('edit_role/<int:pk>', views.edit_role, name='edit_role'),
    path('delete_role/<int:pk>', views.delete_role, name='delete_role'),
    
    path('get_designation/', views.get_designation, name='get_designation'),
    path('post_designation/', views.post_designation, name='post_designation'),
    path('edit_designation/<int:pk>', views.edit_designation, name='edit_designation'),
    
    path('get_designation_head/', views.get_designation_head, name='get_designation_head'),
    path('post_designation_head/', views.post_designation_head, name='post_designation_head'),
    path('edit_designation_head/<int:pk>', views.edit_designation_head, name='edit_designation_head'),
    
    ]