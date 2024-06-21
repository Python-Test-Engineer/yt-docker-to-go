from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):

    now = datetime.now()  # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return HttpResponse(f"<h2>Hello, world! <h2><h2>The time is {date_time}<h2>")


def test(request):

    return render(request, "base.html")
