from django.urls import path

from device import views

urlpatterns = [
    path('list/', views.pcView ),
    path('search_staff', views.searchPcView, name='search-pc'),
    path('register/', views.deviceRegisterView),
    path('edit/<int:device_id>/', views.deviceEditView),
    path('finance/', views.finance),
]