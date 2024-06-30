from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):

    now = datetime.now()  # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    output = f"<div style='width: 600px; margin: 40px auto'>"
    output += f"<h2 style='color:green'>Hello, world! The time is {date_time}</h2>"
    output += f"<p style='font-size: 20px'>Qui irure ea dolore magna sint fugiat sint excepteur adipisicing officia fugiat amet. Exercitation aute labore consectetur aliquip. Eu dolor do nulla culpa id voluptate laborum non. Adipisicing amet ullamco ad nostrud eiusmod laboris ad dolore aliqua velit occaecat enim non mollit.</p>"
    output += "</div>"
    return HttpResponse(output)


def test(request):

    return render(request, "base.html")
