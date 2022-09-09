from django.http import HttpResponse
from django.shortcuts import render

from .form import BookingForm
from .models import Departmets, Doctors


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)


def departments(request):
    dict_depy = {
        'dept': Departmets.objects.all()}
    return render(request, 'departments.html', dict_depy)


def doctors(request):
    dict_do = {
        'doctors': Doctors.objects.all()

    }
    return render(request, 'doctors.html', dict_do)


def contact(request):
    return render(request, 'contact.html')
