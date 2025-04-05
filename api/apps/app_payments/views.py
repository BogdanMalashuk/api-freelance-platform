from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer
from ..app_users.permissions import IsOwner, IsOwnerOrAdmin, IsAdminUser
from rest_framework.permissions import IsAuthenticated


class PaymentListView(generics.ListAPIView):  # get /api/payments/
    serializer_class = PaymentSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class PaymentCreateView(generics.CreateAPIView):  # post /api/payments/
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaymentDeleteView(generics.DestroyAPIView):  # delete /api/payments/<id>/
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsOwnerOrAdmin]


class PaymentsAdminView(generics.ListAPIView):  # get /api/payments/admin/
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminUser]
