from django.urls import path
from .views import UserRegisterView, UserPrivateDetailView, UserPublicDetailView, UserUpdateView, UserListView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('<int:id>/private/', UserPrivateDetailView.as_view(), name='user-private-detail'),
    path('<int:id>/', UserPublicDetailView.as_view(), name='user-public-detail'),
    path('<int:id>/', UserUpdateView.as_view(), name='user-update'),
    path('', UserListView.as_view(), name='user-list'),
]
