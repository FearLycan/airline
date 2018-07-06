from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from flight.models import Flight, Airport, Passenger


def index(request):
    return render(request, 'flight/index.html', {
        'flights': Flight.objects.all(),
    })


def view(request, flight_id):
    try:
        model = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404('Flight does not exist.')

    return render(request, 'flight/view.html', {
        'flight': model,
        'passengers': model.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=model).all()
    })


def book(request, flight_id):
    try:
        passenger_id = int(request.POST['passenger'])  # check if passenger was POST
        passenger = Passenger.objects.get(pk=passenger_id)  # check if passenger exist
        flight = Flight.objects.get(pk=flight_id)  # check if flight exist
    except KeyError:
        return render(request, 'flight/error.html', {'message': 'No selection'})
    except Passenger.DoesNotExist:
        return render(request, 'flight/error.html', {'message': 'No passenger'})
    except Flight.DoesNotExist:
        return render(request, 'flight/error.html', {'message': 'No flight'})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('view', args=(flight_id,)))
