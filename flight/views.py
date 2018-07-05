from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from flight.models import Flight, Airport


def index(request):
    # a = Airport(code='JFK', city='New York City')
    # a.save()
    #
    # b = Airport(code='LHR', city='London')
    # b.save()
    #
    # f = Flight(origin=a, destination=b, duration=415)
    # f.save()

    return render(request, 'flight/index.html', {
        'flights': Flight.objects.all(),
    })
