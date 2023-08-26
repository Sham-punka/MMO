from django.urls import path
from .views import *

urlpatterns = [
    path('announcement/', PostList.as_view(), name='post_list'),
    path('announcement/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('announcement/create/', PostCreate.as_view(), name='post_create'),
    path('announcement/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('announcement/edit/<int:pk>', PostUpdate.as_view(), name='post_edit'),
    path('responses/', ResponseList.as_view(), name='resp_list'),
    path('response/<int:pk>', ResponseDetail.as_view(), name='response'),
    path('response/<int:pk>/accept', response_accept, name='response_accept'),
    path('response/<int:pk>/reject', response_reject, name='response_reject'),
    path('response/<int:pk>/delete', ResponseDelete.as_view(), name='response_delete'),
    path('<int:pk>/response_create', ResponseCreate.as_view(), name='response_create'),
]