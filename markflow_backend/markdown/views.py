from .serializers import DocumentSerializer
from .models import Document
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class CustomLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, id):
        user = User.objects.filter(id=id).first()
        if not user:
            return Response({"detail": "User not found"}, status=404)

        username = user.username
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })
        return Response({"detail": "Invalid credentials"}, status=401)


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Document.objects.all()

        tag_id = self.request.query_params.get('tag_id')
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)