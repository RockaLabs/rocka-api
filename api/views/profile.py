
from rest_framework.decorators import api_view

from domain.models import Rocker
from api.serializers.profiles import RockerSerializer

from api.globals import JSONResponse


@api_view(['GET'])
def rocker_list(request):

	queryset = Rocker.objects.all()
	serializer = RockerSerializer(instance=queryset, many=True)

	return JSONResponse(dict(result=serializer.data))
