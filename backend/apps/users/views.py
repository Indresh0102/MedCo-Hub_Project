from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .models import CustomUser
from .serializer import RegisterSerializer, LoginSerializer
from apps.medicines.permissions import IsAdminOrReadOnly
from rest_framework.permissions import AllowAny

# Register View
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) # check name of serializer
        print("Step 1: Raw request data =>", request.data)
        serializer.is_valid(raise_exception=True)
        print("Step 2: Cleaned data after validation =>", serializer.validated_data)
        user = serializer.save()
        print("Step 3: User created and saved =>", user)
        return Response({
            "message": "User registered successfully",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "user_type": user.user_type,
                "Phone Number": user.phone_number,
            }
        }, status=status.HTTP_201_CREATED)

# Login View
class LoginView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, email=email, password=password)
        print("What Is Inside The User Now--> ", user)
        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            login(request, user)
        return Response({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "user_type": user.user_type,
                "Phone Number": user.phone_number,
            }
        })
