from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer
from ..app_users.permissions import IsOwner, IsOwnerOrAdmin, IsAdminUser
from rest_framework.permissions import IsAuthenticated


class PaymentListView(generics.ListAPIView):  # get /api/payments/my/
    serializer_class = PaymentSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Payment.objects.filter(creator=self.request.user)


class PaymentCreateView(generics.CreateAPIView):  # post /api/payments/
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PaymentDetailView(generics.RetrieveAPIView):  # get /api/payments/<id>/
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsOwnerOrAdmin]


class PaymentsListView(generics.ListAPIView):  # get /api/payments/
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminUser]
