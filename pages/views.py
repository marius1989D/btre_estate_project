from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] #pylint: disable=maybe-no-member
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date') #pylint: disable=maybe-no-member

    # get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True) #pylint: disable=maybe-no-member
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)

