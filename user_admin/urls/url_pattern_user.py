from django.urls import path
from ..views import user_view


urlpatterns = [
    path('get-by-id/<int:id>', user_view.get_user_by_id, name='get-by-id'),
    path('get-all', user_view.get_all_users, name='get-all'),
    path('get-all-active', user_view.get_active_users, name='get-active'),
    path('create', user_view.create_user, name='create'),
    path('update/<int:id>', user_view.update_user, name='update'),
    path('delete/<int:id>', user_view.delete_user, name='delete'),
]