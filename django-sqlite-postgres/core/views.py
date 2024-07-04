from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):

    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    output = f"<div style='width: 600px; margin: 40px auto;font-family: sans-serif'>"
    output += f"<h2 style='color:#676767'>Hello, world! The time is {date_time}</h2>"
    output += f"<h2 style='color:#676767'>Hello, world! The time is {date_time}</h2>"
    output += f"<p style='font-size: 42px;color:red;'>Reload</p>"
    output += "</div>"
    return HttpResponse(output)


def test(request):

    return render(request, "base.html")
