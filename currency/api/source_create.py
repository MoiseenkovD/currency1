from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from currency.models import Source, SourceSerializer
from rest_framework.views import APIView
from django.views.generic import CreateView


class SourceCreate(APIView):
    @csrf_exempt
    def get(self, request):
        source = Source.objects.all()

        return JsonResponse(SourceSerializer(source, many=True).data, safe=False)


# class SourceCreateView(CreateView):
#     success_url = "api/source/create"
#     template_name = "source_c.html"

    @csrf_exempt
    def post(self, request):
        source_url = request.data.get("source_url")
        name = request.data.get("name")
        phone = request.data.get("phone")

        if name is None:
            return HttpResponse("Вы не ввели достаточно информации, повторите попытку", status=400)
        else:
            source = Source(name=name, source_url=source_url, phone=phone)
        source.save()
        return HttpResponseRedirect('/index/')
        # return JsonResponse(SourceSerializer(source).data, status=201)