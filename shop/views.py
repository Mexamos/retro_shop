from django.shortcuts import render

from .models import Offers

def index(request):
    offers = Offers.objects.all()
    context = {'offers': offers}
    return render(request, 'index.html', context)
