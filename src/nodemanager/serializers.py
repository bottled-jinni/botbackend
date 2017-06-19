from rest_framework import serializers
from nodemanager.models import Node
class NodeSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.ReadOnlyField()
	class Meta:
		model  = Node
		fields = ('url','name','infected','rank') 