from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_delete


urlpatterns = [
    path('', post_list, name='post_list'),
    path('post_detail/<int:post_id>/', post_detail, name='post_detail'),
    path('post_create/', post_create, name='post_create'),
    path('post_update/<int:post_id>/', post_update, name='post_update'),
    path('post_delete/<int:post_id>/', post_delete, name='post_delete')
]
