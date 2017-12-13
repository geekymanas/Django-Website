from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This Is The Music App HomePage</h1>")
