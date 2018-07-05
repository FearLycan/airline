from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from flight.models import Flight, Airport


def index(request):
    return render(request, 'flight/index.html', {
        'flights': Flight.objects.all(),
    })


def view(request, flight_id):
    try:
        f = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404('Flight does not exist.')

    return render(request, 'flight/view.html', {
        'flight': f,
    })
