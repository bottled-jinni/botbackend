from django.shortcuts import render
from nodemanager.models import Node
from nodemanager.serializers import NodeSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response
# Create your views here.

class NodeItemViewSet(viewsets.ModelViewSet):
	queryset 			= Node.objects.all()
	serializer_class	= NodeSerializer

	def perform_create(self, serializer):
		#save instance -> get primary key and update url
		instance = serializer.save()
		instance.url = reverse('node-detail', args=[instance.pk], request=self.request)
		instance.save()
