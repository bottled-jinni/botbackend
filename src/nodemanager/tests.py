from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from nodemanager.models import Node

def createNode(client):
	url  = reverse('node-list')
	data = {"name": "vm_test"}
	return client.post(url, data, format='json')

class TestCreateNode(APITestCase):
  """
  Ensure we can create a new node (virtual machine)
  """
  def setUp(self):
    self.response = createNode(self.client) 

  def test_received_201_created_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
  def test_received_location_header_hyperlink(self):
    self.assertRegexpMatches(self.response['Location'], '^http://.+/nodemanager/[\d]+$')