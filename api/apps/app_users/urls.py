from django.urls import path
from .views import (UserRegisterView, UserPrivateDetailView,
                    UserPublicDetailView, UserUpdateView,
                    UserListView, UserDeleteView)


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('<int:pk>/private/', UserPrivateDetailView.as_view(), name='user-private-detail'),
    path('<int:pk>/', UserPublicDetailView.as_view(), name='user-public-detail'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('', UserListView.as_view(), name='user-list'),
]
