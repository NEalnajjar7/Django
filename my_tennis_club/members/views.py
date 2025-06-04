from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from datetime import datetime,date
from django.db.models import Q
from rest_framework import generics





def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mymembers = list(Member.objects.all())
  half = len(mymembers)//2
  first_half = mymembers[:half]
  second_half = mymembers[half:]
 
  template = loader.get_template('template.html')
  context = {
    'first_half': first_half,
        'second_half': second_half,
  }
  return HttpResponse(template.render(context, request)) 

# Example for Function-Based Views(@api_view)
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"})
    elif request.method == 'POST':
        # Echo back the posted data
        return Response({"message": "You posted:", "data": request.data})
    
# Example for Class-Based Views (APIView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloWorldAPIView(APIView):
   def get(self, request):
      return Response({"message": "Hello, world"})
   
   def post(self, request):
      return Response({"message": "You posted", "data": request.data},
                      status=status.HTTP_201_CREATED)

# Example for Generic Class-Based Views
