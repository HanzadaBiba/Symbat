from django.urls import path
from home import views
app_name='home'
urlpatterns=[
    path('',views.index,name='home'),
    path('method/<str:slug>/',views.method_detail,name='method_detail'),
    path('method/<str:slug>/order/',views.order,name='order'),

]