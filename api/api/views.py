from django.http import HttpResponse

def api(request):
    with open('apiOut.txt', 'r') as the_file:
        return HttpResponse(the_file.read())

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
