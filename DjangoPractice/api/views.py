from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def main(request):
    # return HttpResponse("<h1>Hello django!</h1>")
    return JsonResponse({
        "success": "OK!",
        "WOW": 123
    })


def test(request):
    return HttpResponse("Test")
