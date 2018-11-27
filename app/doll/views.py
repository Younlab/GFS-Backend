from rest_framework.response import Response
from rest_framework.views import APIView

from doll.models import Doll


# class DollList(ListAPIView):
#     queryset = Doll.objects.all()
#     serializer_class = DollListSerializer


class DollList(APIView):
    def get(self, request):
        objects = Doll.objects.values('id', 'code_name', 'rank', 'type', 'image')
        return Response(objects)

    def post(self, request, *arge, **kwargs):
        pass
