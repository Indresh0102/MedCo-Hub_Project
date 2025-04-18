from rest_framework import generics, mixins
from rest_framework.permissions import IsAdminUser
from apps.medicines.models import Medicine
from apps.medicines.serializers import MedicineSerializer


# LIST + CREATE
class MedicineListCreateView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]  # Admins only can POST
        return self.create(request, *args, **kwargs)


# RETRIEVE + UPDATE + DELETE
class MedicineDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
