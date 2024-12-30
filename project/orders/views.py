from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from orders.models import SalesOrder

# Create your views here.


def orders_page(request: HttpRequest) -> HttpResponse:
    context = {"orders": SalesOrder.objects.all()}
    response = render(request, "./orders/index.html", context)

    return response
