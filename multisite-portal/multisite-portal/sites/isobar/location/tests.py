from django.test import TestCase
from django.test.client import Client
from sites.isobar.location.models import Country, Agency

class LocationTest(TestCase):
	def test_index(self):
		self.country = Country.objects.create(title='UK', slug='uk')

		self.agency1 =  Agency.objects.create(  title='Agency 1',
												 slug='agency-1', 
												 contact_name='Joe Bloggs',
												 contact_email='joe.bloggs@agency1.com',
												 contact_position='MD', 
												 contact_number='01255 125574', 
												 latitude='51.552181',
												 longitude='-0.141292',
												 country=self.country, 
												 address='Agency 1, London')
		
		self.agency2 =  Agency.objects.create(  title='Agency 2',
												 slug='agency-2', 
												 contact_name='Joe Bloggs',
												 contact_email='joe.bloggs@agency2.com',
												 contact_position='MD', 
												 contact_number='01255 125574', 
												 latitude='51.552181',
												 longitude='-0.141292',
												 country=self.country, 
												 address='Agency 2, London')
		
		self.agency3 =  Agency.objects.create(  title='Agency 3',
												 slug='agency-3', 
												 contact_name='Joe Bloggs',
												 contact_email='joe.bloggs@agency3.com',
												 contact_position='MD', 
												 contact_number='01255 125574', 
												 latitude='51.552181',
												 longitude='-0.141292',
												 country=self.country, 
												 address='Agency 3, London')
		
		c = Client(enforce_csrf_checks=True)
		response = c.get('location_view')
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['agencies']), 3)
			
	def test_country(self):
		self.country = Country.objects.create(title='UK', slug='uk')
		
		c = Client(enforce_csrf_checks=True)
		response = c.get(self.country.get_absolute_url())
		
		self.assertEqual(response.status_code, 200)
		
	def test_agency(self):
		self.country = Country.objects.create(title='UK', slug='uk', )		
		self.agency =  Agency.objects.create(title='Agency 1',
												slug='agency-1', 
												contact_name='Joe Bloggs',
												contact_email='joe.bloggs@agency1.com',
												contact_position='MD', 
												contact_number='01255 125574', 
												latitude='51.552181',
												longitude='-0.141292',
												country=self.country, 
												address='Agency 1, London',)
		
		c = Client(enforce_csrf_checks=True)
		response = c.get(self.agency.get_absolute_url())

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['agency'], self.agency)		