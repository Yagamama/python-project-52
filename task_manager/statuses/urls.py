from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusesView.as_view(), name='statuses_list'),
    path('create/', views.StatusesCreateView.as_view(), name='status_create'),
    path('<int:pk>/update/', views.StatusesUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', views.StatusesDeleteView.as_view(), name='status_delete'),
]