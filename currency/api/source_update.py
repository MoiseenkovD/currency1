from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from currency.models import Source, SourceSerializer
from rest_framework.views import APIView


class SourceUpdate(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            source = Source.objects.get(pk=request.data.get('id'))

            source_url = request.data.get("source_url", source.source_url)
            name = request.data.get("name", source.name)
            phone = request.data.get("phone", source.phone)

            source.source_url = source_url
            source.name = name
            source.phone = phone

            source.save()
        except Source.DoesNotExist:
            return HttpResponse('Такого ID не существует', status=404)

        return JsonResponse(SourceSerializer(source).data)