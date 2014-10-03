"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from apps.common.models import Item
from apps.people.models import Department, Person
from apps.work.models import CaseStudy
from apps.home.models import Layout, LayoutItem
import datetime

class HomeTest(TestCase):
    def test_layout(self):
    	     
   		self.department = Department.objects.create(title='Creative', slug="creative", colour="#fff000")
     
		self.person1 = Person.objects.create(department=self.department, title="Damian Mitchell", slug='damian-mitchell')
		self.person2 = Person.objects.create(department=self.department, title="Seb Royce", slug='seb-royce')
		self.person3 = Person.objects.create(department=self.department, title="Fraser Campbell", slug='fraser-campbell')

  		self.casestudy1 = CaseStudy.objects.create(title='Case Study 1', slug='case-study-1', tagline='Case Study 1 Tagline', date=datetime.date.today())
		self.casestudy2 = CaseStudy.objects.create(title='Case Study 2', slug='case-study-2', tagline='Case Study 3 Tagline', date=datetime.date.today())
		self.casestudy3 = CaseStudy.objects.create(title='Case Study 3', slug='case-study-3', tagline='Case Study 3 Tagline', date=datetime.date.today())
		
		self.layout1 =  Layout.objects.create(item=self.person1, order=1, size=340)
		self.layout2 =  Layout.objects.create(item=self.person2, order=2, size=340)
		self.layout3 =  Layout.objects.create(item=self.person3, order=3, size=340)
		
		self.layout4 =  Layout.objects.create(item=self.casestudy1, order=1, size=340)
		self.layout5 =  Layout.objects.create(item=self.casestudy2, order=2, size=340)
		self.layout6 =  Layout.objects.create(item=self.casestudy3, order=3, size=340)
		
  		c = Client(enforce_csrf_checks=True)
		response = c.get('/')
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['casestudies']), 3)
		self.assertEqual(len(response.context['people']), 3)
		
		
		print response.content