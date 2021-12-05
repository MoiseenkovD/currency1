from django.shortcuts import render, get_object_or_404
from currency.models import Source, Rate
from currency.forms import RateForm
from django.http.response import HttpResponseRedirect, Http404


def rate_list(request):
    rates = Rate.objects.all()

    context = {
        'rates': rates,
     }

    return render(request, 'rate_list.html', context)


def rate_details(request, pk):

    rate = get_object_or_404(Rate, id=pk)

    context = {
        'rate': rate,
     }

    return render(request, 'rate_details.html', context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'form': form,
    }
    return render(request, 'rate_create.html', context)


def rate_update(request, pk):

    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)

    context = {
        'form': form,
    }
    return render(request, 'rate_delete.html', context)


def rate_delete(request, pk):

    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'GET':
        context = {
            'object': rate,
        }
        return render(request, 'rate_delete.html', context)
    elif request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')


def main(request):
    return render(request, "main.html")


def index(request):
    source = Source.objects.all()
    return render(request, "index.html", {
        "source": source
    })


def create(request):
    return render(request, "source_c.html")


def update(request):
    return render(request, "source_u.html")


def delete(request):
    return render(request, "source_d.html")


def get_by_id(request, id):
    source = Source.objects.get(pk=id)
    return render(request, "get_by_id.html", {
        "source": source
    })