from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from shop.models import Product


def main_page(request: HttpRequest):
    products = Product.objects.all()
    return render(
        request,
        "index.html",
        context={"products": products}
    )
