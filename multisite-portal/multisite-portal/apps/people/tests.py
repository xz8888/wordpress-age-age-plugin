"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from apps.common.models import Item
from apps.people.models import Department, Person



class PeopleTest(TestCase):
  	
	def test_people(self):
	
		self.department = Department.objects.create(title='Creative', slug="creative", colour="#fff000")
		
		self.person1 = Person.objects.create(department=self.department, title="Damian Mitchell", slug='damien-mitchell')
		self.person2 = Person.objects.create(department=self.department, title="Seb Royce", slug='seb-royce')
		self.person3 = Person.objects.create(department=self.department, title="Fraser Campbell", slug='fraser-campbell')

		c = Client(enforce_csrf_checks=True)
		response = c.get('/people/')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['people']), 3)


	def test_person(self):
	
		self.department = Department.objects.create(title='Creative', slug="creative", colour="0xfff000")
		self.person = Person.objects.create(department=self.department, title="Damian Mitchell", slug='damien-mitchell')
		
		c = Client(enforce_csrf_checks=True)
		response = c.get(self.person.get_absolute_url())
		
		self.assertEqual(response.status_code, 200)
		self.failUnlessEqual(response.context['person'], self.person)
	
	def test_departments(self):
		
		self.department1 = Department.objects.create(title='Creative', slug="creative", colour="0xfff000")
		self.department2 = Department.objects.create(title='Development', slug="development", colour="0xfff000")
		self.department3 = Department.objects.create(title='Design', slug="design", colour="0xfff000")

		c = Client(enforce_csrf_checks=True)
		response = c.get('/departments/')
			
		print response.content
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['departments']), 3)
	
	def test_department(self):
		self.department = Department.objects.create(title='Creative', slug="creative", colour="0xfff000")
		
		self.person1 = Person.objects.create(department=self.department, title="Damian Mitchell", slug='damien-mitchell')
		self.person2 = Person.objects.create(department=self.department, title="Seb Royce", slug='seb-royce')
		self.person3 = Person.objects.create(department=self.department, title="Fraser Campbell", slug='fraser-campbell')
		
		c = Client(enforce_csrf_checks=True)
		response = c.get(self.department.get_absolute_url())
		response.status_code
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['department'], self.department)
		self.assertEqual(len(response.context['people']), 3)
		