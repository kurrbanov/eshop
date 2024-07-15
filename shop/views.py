from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from shop.models import Product
from shop.forms import CustomUserCreationForm


def main_page(request: HttpRequest):
    products = Product.objects.all()
    return render(
        request,
        "index.html",
        context={
            "products": products,
            "is_authenticated": request.user.is_authenticated,
        },
    )


def register_page(request: HttpRequest):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main-page")

    form = CustomUserCreationForm()
    return render(
        request,
        "registration.html",
        context={"form": form}
    )
