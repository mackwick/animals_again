from .models import Turtle
from rest_framework import viewsets, permissions
from .serializer import TurtleSerializer

class TurtleViewSet(viewsets.ModelViewSet):
    queryset=Turtle.objects.all().order_by('id')
    serializer_class=TurtleSerializer
    permission_classes=[permissions.AllowAny]