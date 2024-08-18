from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
#from .serializers import MessageSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

	routes = [
		{
			'Endpoint': '/notes/',
			'method': 'GET',
			'body': None, 
			'description': 'Returns an array of notes'
		},
		{
			'Endpoint': '/notes/id',
			'method': 'GET',
			'body': None, 
			'description': 'Returns a single note object'
		},		
		{
			'Endpoint': '/notes/create/',
			'method': 'POST',
			'body': {'body': ""}, 
			'description': 'Create a note with data sent in post request'
		},
		{
			'Endpoint': '/notes/id/update/',
			'method': 'PUT',
			'body': {'body': ""}, 
			'description': 'Create a note with data sent in post request'
		},
		{
			'Endpoint': '/notes/id/delete/',
			'method': 'DELETE',
			'body': None, 
			'description': 'Delete an existing note'
		}
	]
	#return JsonResponse(routes, safe=False)
	return Response(routes)

@api_view(['GET'])
def getNotes(request):
	return Response("Julio Notes here")

"""
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get']
"""