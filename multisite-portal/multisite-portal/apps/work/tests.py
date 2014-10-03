from django.test import TestCase
from django.test.client import Client
from apps.common.models import Item
from apps.work.models import CaseStudy, Award, Quote, Link, Text
import datetime

class WorkTest(TestCase):
	
    def test_casestudy(self):
    
    	self.casestudy = CaseStudy.objects.create( title='Case Study 1', \
													slug='case-study-1', \
													date=datetime.date.today(), \
													body="Body")    	
    	
    	self.award = Award.objects.create( title='Award 1', \
											description= 'Award 1 description', \
											image='/images/test.jpg', \
											date=datetime.date.today(), \
											case_study=self.casestudy, \
											body="Award body")
    	
    	c  = Client(enforce_csrd_checks=True)
    	response = c.get(self.casestudy.get_absolute_url())
    	
    	self.assertEqual(response.status_code, 200)
    	self.assertEqual(response.context['casestudy'], self.casestudy)

    def test_casestudies(self):
		
		self.casestudy1 = CaseStudy.objects.create(title='Case Study 1', 
													slug='case-study-1', \
													date=datetime.date.today())
		
		self.casestudy2 = CaseStudy.objects.create(title='Case Study 2', \
													slug='case-study-2', \
													date=datetime.date.today())
		
		self.casestudy3 = CaseStudy.objects.create(title='Case Study 3', \
													slug='case-study-3', \
													date=datetime.date.today())
		
		c = Client(enforce_csrf_checks=True)
		response = c.get('/work/')
    	
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['casestudies']), 3)

		