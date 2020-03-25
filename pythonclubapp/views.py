from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')

def getresources(request):
    type_list=Resource.objects.all()
    return render(request, 'pythonclubapp/types.html', {'type_list':type_list})

