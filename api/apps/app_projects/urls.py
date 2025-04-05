from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name='list-project'),
    path('', ProjectCreateView.as_view(), name='create-project'),
    path('<int:id>/', ProjectDetailView.as_view(), name='detail-project'),
    path('<int:id>/', ProjectUpdateView.as_view(), name='update-project'),
    path('<int:id>/', ProjectDeleteView.as_view(), name='delete-project'),
]
