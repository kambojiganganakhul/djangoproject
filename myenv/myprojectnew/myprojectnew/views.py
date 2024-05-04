from django.http import HttpResponseNotFound
def handle404(request,exception):
    return HttpResponse("<h1 style='color:red'>page not found</h1>",status=404)

    