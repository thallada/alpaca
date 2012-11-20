from django.shortcuts import render_to_response
from alpaca_viewer.models import Alpaca
from random import randint


def viewer(request):
    """Displays a random alpaca"""
    # Note: I'm not using Alpaca.objects.order_by('?')[0] because it's been known
    # to be slow on some databases (MySQL) with a large dataset, so I'm playing
    # it safe and just accessing a random index from .all()
    alpaca = None
    size = Alpaca.objects.count()
    if size > 0:
        i = randint(0, size-1)
        alpaca = Alpaca.objects.all()[i]
    return render_to_response('viewer.html', {'alpaca': alpaca})
