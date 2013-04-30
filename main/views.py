from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from main.models import Customer
from mishloha.util.lib import response_json


def home(request):
    return render_to_response(
        'home.html',
        {'customers': Customer.objects.all()},
        context_instance=RequestContext(request)
    )