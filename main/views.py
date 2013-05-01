from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from main.models import Customer
from mishloha.util.lib import response_json


def home(request):
    return render_to_response(
        'home.html',
        {'customers': Customer.objects.all()},
        context_instance=RequestContext(request)
    )


def details(request, cust_id):
    customer = get_object_or_404(Customer, pk=cust_id)
    return response_json({
        'email': customer.email,
        'company_name': customer.company_name,
    })