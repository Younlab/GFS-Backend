from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from doll.serializer import DollListSerializer
from .models import Doll


class DollList(ListAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollListSerializer

# class DollList(APIView):
#     def get_object(self):
#         return Doll.objects.all()
#
#     def get(self, request, format=None):
#         # values('id', 'code_name', 'rank', 'type', 'image')
#         objects = self.get_object()
#         serializer = DollListSerializer(data=objects)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *arge, **kwargs):
#         pass
