from django.urls import path

from step import views

urlpatterns = [
    path('list/', views.warehouseView ),
    path('search_warehouse/', views.searchwarehouseView, name='search-warehouse'),
    path('prepared_list/', views.preparedView ),
    path('search_prepared/', views.searchpreparedView, name='search-prepared'),
    path('inuse_list/', views.inUseView ),
    path('search_inuse/', views.searchinUseView, name='search-inuse'),
    path('retired_list/', views.retiredView ),
    path('search_retired/', views.searchretiredView, name='search-retired'),
    path('retired_idle/', views.retiredIdleView),
    path('retired_recycle/', views.retiredRecycleView),
    path('prepared/', views.preparedTaskView),
    path('inuse/', views.inuseTaskView),
    path('warehouse/', views.warehouseTaskView),
    path('warehouse_register/',views.warehouseRegisterView),
    path('prepared_register/', views.preparedRegisterView),
    path('inuse_register/', views.inuseRegisterView),
    path('retired_register/', views.retiredRegisterView),
    path('edit/<int:warehouse_id>/', views.warehouseEditView),
    path('prepared_edit/<int:prepared_id>/', views.preparedEditView),
    path('inuse_edit/<int:inuse_id>/', views.inuseEditView),
    path('retired_edit/<int:retired_id>/', views.retiredEditView),
    
    
]