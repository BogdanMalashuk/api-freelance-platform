from django.urls import path
from .views import PaymentListView, PaymentCreateView, PaymentDetailView, PaymentsListView

urlpatterns = [
    path('my/', PaymentListView.as_view(), name='list-owner-payment'),
    path('create/', PaymentCreateView.as_view(), name='create-payment'),
    path('<int:id>/', PaymentDetailView.as_view(), name='detail-payment'),
    path('', PaymentsListView.as_view(), name='list-all-payment'),
]
