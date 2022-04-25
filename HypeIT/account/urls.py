from django.urls import path

from account import views

urlpatterns = [
    path('extern/', views.staffView ),
    path('search_staff/', views.searchStaffView, name='search-staff'),
    path('staff_register/', views.staffRegisterView, name='staffreg'),
    path('edit/<int:staff_id>/', views.staffEditView),
    path('delete/<int:staff_id>/', views.staffDeleteView, name='delete-staff'),
]