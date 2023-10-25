from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('add_user', views.add_user, name='add_user'),
    path('edit_user/<int:user_id>', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>', views.delete_user, name='delete_user'),

    path('groups', views.groups, name='groups'),
    path('groups/add_group', views.add_group, name='add_group'),
    path('groups/edit_group/<int:group_id>', views.edit_group, name='edit_group'),
    path('groups/delete_group/<int:group_id>', views.delete_group, name='delete_group')
]