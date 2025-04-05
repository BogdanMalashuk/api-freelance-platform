from django.urls import path
from .views import PaymentListView, PaymentCreateView, PaymentDeleteView, PaymentDetailView, PaymentsListView

urlpatterns = [
    path('/', PaymentListView.as_view(), name='owner-payment-list'),
    path('/', PaymentCreateView.as_view(), name='create-payment'),
    path('/<int:id>/', PaymentDetailView.as_view(), name='detail-payment'),
    path('/<int:id>/', PaymentDeleteView.as_view(), name='delete-payment'),
    path('/', PaymentsListView.as_view(), name='all-payment-list'),
]
