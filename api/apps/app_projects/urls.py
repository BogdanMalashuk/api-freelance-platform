from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name='list-project'),
    path('create/', ProjectCreateView.as_view(), name='create-project'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail-project'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='update-project'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete-project'),
]
