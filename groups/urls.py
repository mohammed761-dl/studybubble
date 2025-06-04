from django.urls import path
from . import views
from .views import join_group, GroupDetailView

urlpatterns = [
    path('', views.GroupListView.as_view(), name='group_list'),
    path('create/', views.GroupCreateView.as_view(), name='group_create'),
    path('join/<int:group_id>/', join_group, name='join_group'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
]