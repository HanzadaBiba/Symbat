from django.contrib.auth import views as auth_views
from django.urls import path,include
from account import views
app_name='registration'
urlpatterns=[
path('', include('django.contrib.auth.urls')),
path('register/', views.register, name='register'),
]