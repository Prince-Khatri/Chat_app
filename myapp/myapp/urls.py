from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('chat/', views.chat_home, name='chat_home'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/', views.get_messages, name='get_messages'),
    path('get_contacts/', views.get_contacts, name='get_contacts'),

    path('get_all_groups/', views.get_all_groups, name='get_all_groups'),
    path('join_group/', views.join_group, name='join_group'),
]
