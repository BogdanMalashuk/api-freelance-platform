from django.urls import path
from .views import PaymentListView, PaymentCreateView, PaymentDeleteView, PaymentDetailView, PaymentsListView

urlpatterns = [
    path('', PaymentListView.as_view(), name='list-owner-payment'),
    path('create/', PaymentCreateView.as_view(), name='create-payment'),
    path('<int:id>/', PaymentDetailView.as_view(), name='detail-payment'),
    path('<int:id>/delete', PaymentDeleteView.as_view(), name='delete-payment'),
    path('', PaymentsListView.as_view(), name='list-all-payment'),
]
