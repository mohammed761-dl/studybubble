from django.urls import path
from .views import (GroupListView, GroupCreateView, GroupDetailView, GroupUpdateView, GroupDeleteView, join_group,
                    leave_group, my_groups, group_detail)

urlpatterns = [
    path('', GroupListView.as_view(), name='group-list'),
    path('create/', GroupCreateView.as_view(), name='group-create'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('<int:pk>/update/', GroupUpdateView.as_view(), name='group-update'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    path('<int:pk>/join/', join_group, name='group-join'),
    path('<int:pk>/leave/', leave_group, name='group-leave'),
    path('my/', my_groups, name='my-groups'),
    path('groups/<int:pk>/', group_detail, name='group-detail'),

]
