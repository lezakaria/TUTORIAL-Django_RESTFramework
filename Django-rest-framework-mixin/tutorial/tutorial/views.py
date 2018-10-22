from django.http import HttpResponse

def home(request):
    message='welcome to the API'
    return HttpResponse(message)