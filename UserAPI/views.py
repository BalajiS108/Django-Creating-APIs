from django.http import HttpResponse, JsonResponse


def homepage(request):
    details = [{'name': 'Balaji', 'age': 31}]
    # return HttpResponse("Hello This is Homepage")
    return JsonResponse(details, safe=False)
