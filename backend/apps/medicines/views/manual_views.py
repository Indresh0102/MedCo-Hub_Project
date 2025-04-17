from rest_framework.views import APIView
from rest_framework.response import Response
from medicines.models import Medicine
from medicines.serializers import MedicineSerializer

class MedicineListAPIView(APIView):
    def get(self, request):
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data)
