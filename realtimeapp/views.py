from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def index(request):
    return render(request,'realtimeapp/index.html')
    #return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def feedback(request):
    # email = request.POST.get("email", False)
    # feedback = request.POST.get("feedback", False)
    # email = request.POST['email']
    # feedback = request.POST['feedback']
    results = {}
    # results['email'] = email
    # results['feedback'] = feedback
    results= json.loads(request.body)
    return JsonResponse(results)


