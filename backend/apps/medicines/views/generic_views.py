from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
from apps.medicines.permissions import IsAdminOrReadOnly
from apps.medicines.models import Medicine
from apps.medicines.serializers import MedicineSerializer


# LIST + CREATE
class MedicineListCreateView(generics.ListCreateAPIView):

    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'brand']
    filterset_fields = ['price', 'mg', 'expiry_date', 'stock', 'category']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# RETRIEVE + UPDATE, PARTIAL_UPDATE + DELETE
class MedicineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
