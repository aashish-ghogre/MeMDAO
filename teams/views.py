from django.http import HttpResponse
from teams.models import Test
def home(request):
    return HttpResponse('Hello, World!')

def test(request):
    return HttpResponse(Test.objects.all()[0])