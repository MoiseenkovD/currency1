from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from currency.models import Source, SourceSerializer
from rest_framework.views import APIView


class SourceDelete(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            source = Source.objects.get(pk=request.data.get('id'))

            source.delete()
            return JsonResponse(SourceSerializer(source).data)
        except Source.DoesNotExist:
            return HttpResponse('Такого ID не существует', status=404)