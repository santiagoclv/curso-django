from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import HttpResponse

# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'home/main.html')


def hello(request):
    count = request.session.get("count", 0)
    count = count + 1
    request.session["count"] = count
    response = HttpResponse("view count=" + str(count))
    response.set_cookie('dj4e_cookie', '8d4112ce', max_age=1000)
    return response